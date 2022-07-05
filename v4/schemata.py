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
    invalidation_service = weighted_url_list()
    issuer_cipher_suite = fields.String(required=True)
    issuer_public_master_key = fields.Nested(PublicKey(), required=True)
    protocol_version = fields.String(required=True)
    renewal_service = weighted_url_list()
    type = TypeField("cdd")
    validation_service = weighted_url_list()


class CDDC(Schema):
    cdd = fields.Nested(CDD(), required=True)
    signature = BigInt(required=True)
    type = TypeField("cdd certificate")

class MintKey(Schema):
    cdd_serial = fields.Integer(required=True)
    coins_expiry_date = fields.DateTime(required=True)
    denomination = fields.Integer(required=True)
    id =  BigInt(required=True)
    issuer_id =  BigInt(required=True)
    public_mint_key =  fields.Nested(PublicKey(), required=True)
    sign_coins_not_after = fields.DateTime(required=True)
    sign_coins_not_before = fields.DateTime(required=True)
    type = TypeField("mint key")

class MintKeyCertificate(Schema):
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
    reference = fields.String(required=True)
    blinded_payload_hash = BigInt(required=True)
    mint_key_id = BigInt(required=True)
    type = TypeField("blinded payload hash")

class BlindSignature(Schema):
    reference = fields.String(required=True)
    blind_signature = BigInt(required=True)
    type = TypeField("blind signature")

if __name__ == '__main__':
    pprint(JSONSchema().dump(Coin()))