import hashlib
import json
import re

import oc_crypto
import schemata


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(item)
        return self[item]


def to_attr_dict(dct):
    out = AttrDict()
    for k, v in sorted(dct.items()):
        out[k] = to_attr_dict(v) if isinstance(v, dict) else v
    return out


class Container:
    schema = None

    def __init__(self, data=None, _add_type=False, **kwargs):

        if data:
            if type(data) == str:
                self.loads(data)
            else:
                self.data = to_attr_dict(data)
        elif kwargs:
            self.data = to_attr_dict(kwargs)
        else:
            self.data: AttrDict = self._default_data

        if _add_type:
            self._add_type()

    def _add_type(self):
        if 'type' not in self.data:
            self.data.type = self.schema.fields['type'].validate.comparable

    def __getattr__(self, item):
        return getattr(self.data, item)

    @property
    def _default_data(self) -> AttrDict:
        return AttrDict()

    def load(self, data):
        self.data = to_attr_dict(self.schema.load(data))

    def loads(self, data):
        self.data = to_attr_dict(self.schema.loads(data))

    def dumps(self, indent=None):
        output = json.dumps(json.loads(self.schema.dumps(self.data)), indent=indent, sort_keys=True)

        def replace_int_list(match):
            inner = match.group(1)
            inner = re.sub(r'\s+', ' ', inner).strip()
            return f'[{inner}]'

        def replace_list_space(match):
            print(match.group(1))
            print('-' * 20)
            lists = match.group(1)
            appendix = match.group(2)
            lists = re.sub(r'\s+', ' ', lists).strip()
            out = f'": [{lists}]{appendix}'
            return out

        if indent and 1:
            output = re.sub(r'\[([^{\]]*)\]', replace_int_list, output, flags=re.S)
            output = re.sub(r'\]\s+\],', ']\n      ],', output)
            output = re.sub(r'\[\[', '[\n        [', output)
            output = output.replace('[ ', '[')
            # output = re.sub(r'\[([\s,\d]+)\]',replace_int_list, output, flags=re.S)
            # output = re.sub(r'": \[(.*?)\]((\s+?})?,\s+"[^"]+?": )', replace_list_space, output, flags=re.S)
            # output = re.sub(r'\[\s+\[\s+',r'[[',output, flags=re.S)
            # output = re.sub(r'(\d+),\s{6}',r'\1,',output)
            # output = re.sub(r'\]\s+\]', r']]', output, flags=re.S)
            # output = re.sub(r'\[(\s+)(\d+),\s+"(.*?)"\s+\]',r'[\2,"\3"]',output)
            # output = re.sub(r'\],\s+\[',r'],[',output)

            # output = re.sub(r'": \[\s+', '": [', output, flags=re.S)
            # output = re.sub(r'",\s+', '", ', output, flags=re.S)
            # output = re.sub(r'"\s+]', '"]', output, flags=re.S)
            ...
        return output

    def __str__(self):
        # convert to a nice json representation
        return self.dumps(2)

    def __repr__(self):
        return str(self)

    def hash(self):
        return int.from_bytes((hashlib.sha256(self.dumps().encode()).digest()), 'big')

    def set_id(self, key_field):
        pk = PublicKey(self.data[key_field])
        self.data.id = pk.hash()
        return self.data.id


class SignedContainer(Container):
    document_class = None

    def __init__(self, data=None, document_data=None, **kwargs):
        super(SignedContainer, self).__init__(data, **kwargs)
        if document_data:
            if isinstance(document_data, Container):
                self.data[self.document_field] = document_data.data
            else:
                self.data[self.document_field] = document_data

    @property
    def _default_data(self):
        data = {'signature':         None,
                self.document_field: None,
                'type':              self.schema.fields['type'].validate.comparable}
        return AttrDict(data)

    @property
    def document_field(self):
        return [k for k in self.schema.fields.keys() if k not in ['signature', 'type']][0]

    def sign(self, private_key):
        document = self.document_class(self.data[self.document_field]).dumps().encode()
        signature = oc_crypto.sign(document, private_key, 'SHA-256')
        self.data.signature = int.from_bytes(signature, 'big')
        return self.data.signature


class Request(Container):
    ...


class Response(Container):

    @property
    def document_field(self):
        return [k for k in self.schema.fields.keys() if k not in ['message_reference', 'status_code',
                                                                  'status_description', 'type']][0]

    @property
    def _default_data(self):
        data = {'message_reference':  None,
                'status_code':        200,
                'status_description': 'ok',
                self.document_field:  None,
                'type':               self.schema.fields['type'].validate.comparable}
        return AttrDict(data)


class PublicKey(Container):
    schema = schemata.PublicKey()




class CDD(Container):
    schema = schemata.CDD()


class CDDC(SignedContainer):
    schema = schemata.CDDC()
    document_class = CDD


class MintKey(Container):
    schema = schemata.MintKey()


class MintKeyCertificate(SignedContainer):
    schema = schemata.MintKeyCertificate()
    document_class = MintKey

    @property
    def public_key(self):
        return oc_crypto.PublicKey(self.mint_key.public_mint_key.modulus,
                                   self.mint_key.public_mint_key.public_exponent)


class Payload(Container):
    schema = schemata.Payload()


class Coin(SignedContainer):
    schema = schemata.Coin()
    document_class = Payload


class Blind(Container):
    schema = schemata.Blind()


class BlindSignature(Container):
    schema = schemata.BlindSignature()


class RequestCDDSerial(Request):
    schema = schemata.RequestCDDSerial()


class ResponseCDDSerial(Response):
    schema = schemata.ResponseCDDSerial()


class RequestCDDC(Request):
    schema = schemata.RequestCDDC()


class ResponseCDDC(Response):
    schema = schemata.ResponseCDDC()


class RequestMintKeyCertificates(Request):
    schema = schemata.RequestMintKeyCertificates()


class ResponseMintKeyCertificates(Response):
    schema = schemata.ResponseMintKeyCertificates()


class RequestMinting(Request):
    schema = schemata.RequestMinting()


class ResponseMinting(Response):
    schema = schemata.ResponseMinting()


class CoinStack(Container):
    schema = schemata.CoinStack()


class RequestRedeeming(Container):
    schema = schemata.RequestRedeeming()


class RequestRenewal(Container):
    schema = schemata.RequestRenewal()
