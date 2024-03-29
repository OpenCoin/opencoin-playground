import inspect
import json
import sys
from pprint import pprint

from marshmallow import Schema, fields, validate
from marshmallow_jsonschema import JSONSchema


class BigInt(fields.Integer):

    def _serialize(self, value, attr, obj, **kwargs):
        return "" if value is None else hex(value)[2:]

    def _deserialize(self, value, attr, data, **kwargs):
        return int(value, 16)


def weighted_url_list():
    return fields.List(fields.Tuple((fields.Integer(), fields.String())), required=True)


def TypeField(string):
    return fields.String(validate=validate.Equal(string),
                         dump_default=string,
                         required=True)


class PublicKey(Schema):
    modulus = BigInt(required=True)
    public_exponent = fields.Integer(required=True)
    type = TypeField("rsa public key")


class CDD(Schema):
    additional_info = fields.String(required=True)
    cdd_expiry_date = fields.DateTime(required=True)
    cdd_location = fields.Url(required=True)
    cdd_serial = fields.Integer(required=True)
    cdd_signing_date = fields.DateTime(required=True)
    currency_divisor = fields.Integer(required=True)
    currency_name = fields.String(required=True)
    denominations = fields.List(fields.Integer(), required=True)
    id = BigInt(required=True)
    info_service = weighted_url_list()
    issuer_cipher_suite = fields.String(required=True)
    issuer_public_master_key = fields.Nested(PublicKey(), required=True)
    mint_service = weighted_url_list()
    protocol_version = fields.String(required=True)
    redeem_service = weighted_url_list()
    renew_service = weighted_url_list()
    type = TypeField("cdd")


class CDDC(Schema):
    cdd = fields.Nested(CDD(), required=True)
    signature = BigInt(required=True)
    type = TypeField("cdd certificate")


class MintKey(Schema):
    cdd_serial = fields.Integer(required=True)
    coins_expiry_date = fields.DateTime(required=True)
    denomination = fields.Integer(required=True)
    id = BigInt(required=True)
    issuer_id = BigInt(required=True)
    public_mint_key = fields.Nested(PublicKey(), required=True)
    sign_coins_not_after = fields.DateTime(required=True)
    sign_coins_not_before = fields.DateTime(required=True)
    type = TypeField("mint key")


class MKC(Schema):
    mint_key = fields.Nested(MintKey(), required=True)
    signature = BigInt(required=True)
    type = TypeField("mint key certificate")


class Payload(Schema):
    cdd_location = fields.Url(required=True)
    denomination = fields.Integer(required=True)
    issuer_id = BigInt(required=True)
    mint_key_id = BigInt(required=True)
    protocol_version = fields.String(required=True)
    serial = BigInt(required=True)
    type = TypeField("payload")


class Coin(Schema):
    payload = fields.Nested(Payload(), required=True)
    signature = BigInt(required=True)
    type = TypeField("coin")


class Blind(Schema):
    blinded_payload_hash = BigInt(required=True)
    mint_key_id = BigInt(required=True)
    reference = fields.String(required=True)
    type = TypeField("blinded payload hash")


class BlindSignature(Schema):
    blind_signature = BigInt(required=True)
    reference = fields.String(required=True)
    type = TypeField("blind signature")


# -------------- Messages ------------------------

class Request(Schema):
    message_reference = fields.Integer(required=True)


class Response(Schema):
    message_reference = fields.Integer(required=True)
    status_code = fields.Integer(requried=True, dump_default=200)
    status_description = fields.String(required=True, dump_default="ok")


class RequestCDDSerial(Request):
    type = TypeField("request cdd serial")


class ResponseCDDSerial(Response):
    cdd_serial = fields.Integer(required=True)
    type = TypeField("response cdd serial")


class RequestCDDC(Request):
    cdd_serial = fields.Integer(required=True)
    type = TypeField("request cddc")


class ResponseCDDC(Response):
    cddc = fields.Nested(CDDC(), required=True)
    type = TypeField("response cddc")


class RequestMKCs(Request):
    denominations = fields.List(fields.Integer(), required=True)
    mint_key_ids = fields.List(BigInt(), required=True)
    type = TypeField("request mint key certificates")


class ResponseMKCs(Response):
    keys = fields.List(fields.Nested(MKC()), required=True)
    type = TypeField("response mint key certificates")


class RequestMint(Request):
    blinds = fields.List(fields.Nested(Blind()), required=True)
    transaction_reference = BigInt(required=True)
    type = TypeField("request mint")


class ResponseMint(Response):
    blind_signatures = fields.List(fields.Nested(BlindSignature()), required=True)
    type = TypeField("response mint")


class CoinStack(Schema):
    coins = fields.List(fields.Nested(Coin()), required=True)
    subject = fields.String(required=True)
    type = TypeField("coinstack")


class RequestRenew(Request):
    transaction_reference = BigInt(required=True)
    coins = fields.List(fields.Nested(Coin()), required=True)
    blinds = fields.List(fields.Nested(Blind()), required=True)
    type = TypeField("request renew")


class RequestRedeem(Request):
    coins = fields.List(fields.Nested(Coin()), required=True)
    type = TypeField("request redeem")


class ResponseRedeem(Response):
    type = TypeField("response redeem")


class ResponseDelay(Response):
    status_code = fields.Integer(requried=True, dump_default=300)
    type = TypeField("response delay")


class RequestResume(Request):
    transaction_reference = BigInt(required=True)
    type = TypeField("request resume")

# 'register' all our schemata
__all__ = []
type2schema = {}

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj) and issubclass(obj, Schema) and obj.__module__ in ['__main__','schemata']:
        __all__.append(obj.__name__)
        if typ := obj._declared_fields.get('type'):
            typname = typ.validate.comparable
            type2schema[typname] = obj

def all_json_schema_dict():
    def tuple_mapping(self):
        return {'type':'array',
                'prefixItems': [{'type':'number'},
                                {'type':'string'}]}

    fields.Tuple._jsonschema_type_mapping = tuple_mapping

    all = {'$schema': "http://json-schema.org/draft-07/schema#",
           'definitions': {}}
    for typename, schema in type2schema.items():
        j = JSONSchema()
        s = schema()
        js = j.dump(s)
        all['definitions'].update(js['definitions'])
    return all


if __name__ == '__main__':

    print(json.dumps(all_json_schema_dict(), indent=2))

    # print('\n'.join([f'  {typename}' for typename in type2schema]))

