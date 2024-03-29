import hashlib
import json
import re

import schemata

from attr_dict import AttrDict, to_attr_dict


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
        return output

    def __str__(self):
        # convert to a nice json representation
        return self.dumps(2)

    def __repr__(self):
        return str(self)

    def hash(self, hasher='sha1'):
        return int.from_bytes((getattr(hashlib,hasher)(self.dumps().encode()).digest()), 'big')

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
        document = self.document_class(self.data[self.document_field]).dumps(2)
        signature = int.from_bytes(private_key.sign(document),'big')
        self.data.signature = signature
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


class MKC(SignedContainer):
    schema = schemata.MKC()
    document_class = MintKey

class Payload(Container):
    schema = schemata.Payload()


class Coin(SignedContainer):
    schema = schemata.Coin()
    document_class = Payload


class Blind(Container):
    schema = schemata.Blind()


class BlindSignature(Container):
    schema = schemata.BlindSignature()


class RequestCDDCSerial(Request):
    schema = schemata.RequestCDDSerial()


class ResponseCDDCSerial(Response):
    schema = schemata.ResponseCDDSerial()


class RequestCDDC(Request):
    schema = schemata.RequestCDDC()


class ResponseCDDC(Response):
    schema = schemata.ResponseCDDC()


class RequestMKCs(Request):
    schema = schemata.RequestMKCs()


class ResponseMKCs(Response):
    schema = schemata.ResponseMKCs()


class RequestMint(Request):
    schema = schemata.RequestMint()


class ResponseMint(Response):
    schema = schemata.ResponseMint()


class CoinStack(Container):
    schema = schemata.CoinStack()


class RequestRenew(Container):
    schema = schemata.RequestRenew()


class RequestRedeem(Container):
    schema = schemata.RequestRedeem()

class ResponseRedeem(Container):
    schema = schemata.ResponseRedeem()

class ResponseDelay(Container):
    schema = schemata.ResponseDelay()

class RequestResume(Container):
    schema = schemata.RequestResume()