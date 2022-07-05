import schemata
import hashlib
import json
import oc_crypto

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __getattr__(self, item):
        return self[item]


def to_attr_dict(dct):
    out = AttrDict()
    for k, v in sorted(dct.items()):
        out[k] = to_attr_dict(v) if isinstance(v, dict) else v
    return out


class Container:
    schema = None

    def __init__(self, data=None):
        if data:
            if type(data) == str:
                self.loads(data)
            else:
                self.data = to_attr_dict(data)
        else:
            self.data = self._default_data

    @property
    def _default_data(self):
        return AttrDict()

    def load(self, data):
        self.data = to_attr_dict(self.schema.load(data))

    def loads(self, data):
        self.data = to_attr_dict(self.schema.loads(data))

    def dumps(self):
        return json.dumps(json.loads(self.schema.dumps(self.data)), indent=2, sort_keys=True)

    def __str__(self):
        # convert to a nice json representation
        return self.dumps()

    def __repr__(self):
        return self.__str__()

    def hash(self):
        return int.from_bytes((hashlib.sha256(self.dumps().encode()).digest()), 'big')

    def set_id(self, key_field):
        pk = PublicKey(self.data[key_field])
        self.data.id = pk.hash()
        return self.data.id


class SignedContainer(Container):
    document_class = None

    def __init__(self, data=None, document_data=None):
        super(SignedContainer, self).__init__(data)
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


class Payload(Container):
    schema = schemata.Payload()


class Coin(SignedContainer):
    schema = schemata.Coin()
    document_class = Payload


class Blind(Container):
    schema = schemata.Blind()

class BlindSignature(Container):
    schema = schemata.BlindSignature()
