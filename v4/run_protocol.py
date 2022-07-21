import datetime
import os
from itertools import count


import containers
import oc_crypto
from attr_dict import AttrDict
import json

import random

###################### SETUP #########################
cipher_name = 'INSECURE-RSA'
key_length = 256
rand_length = 128
hasher = 'sha1'

random.seed(1)
######################################################

class DummyIssuer:

    def __init__(self):
        self.cddcs = {}  # serial: cddc
        self.mkc = {}  # mintkey_id: mkc
        self.mkc_private = {}  # mintkey_id: private key

    def sign(self, blind):
        mk_id = blind.mint_key_id
        bsignature = oc_crypto.sign_blind(blind.blinded_payload_hash,
                                          self.mkc_private[mk_id][1])
        return create(containers.BlindSignature,
                      blind_signature=bsignature,
                      reference=blind.reference)

    def sum_blinds(self, blinds):
        amount = 0
        for blind in blinds:
            mk_id = blind.mint_key_id
            mkc = self.mkc[mk_id]
            amount += mkc.mint_key.denomination
        return amount


class DummyWallet:

    def __init__(self):
        self.cddcs = {}  # serial: cddc
        self.mkc = {}  # mintkey_id: mkc
        self.mkc_by_denomination = {}  # denomination: mkc
        self.payloads = {}  # reference: payload
        self.blinds = {}  # reference: blind
        self.blinds_private = {}  # reference: (bf, bi)
        self.coins = {}  # reference: coin

    def add_mkc(self, mkc):
        if not isinstance(mkc, containers.Container):
            mkc = containers.MKC(mkc)
        self.mkc[mkc.mint_key.id] = mkc
        self.mkc_by_denomination[mkc.mint_key.denomination] = mkc

    def prepare_blind(self, reference, denomination):
        serial = oc_crypto.getrandbits(rand_length)
        mkc = self.mkc_by_denomination[denomination]
        payload = create(containers.Payload,
                         protocol_version=cdd.data.protocol_version,
                         issuer_id=cdd.data.id,
                         cdd_location=cdd.data.cdd_location,
                         denomination=denomination,
                         mint_key_id=mkc.mint_key.id,
                         serial=serial)
        self.payloads[reference] = payload

        mk_public = mkc.public_key

        bf, bi = oc_crypto.get_blinding_factors(mk_public)
        blinded = oc_crypto.blind_message(payload.hash(), bf, mk_public)
        blind = create(containers.Blind,
                       reference=reference,
                       blinded_payload_hash=blinded,
                       mint_key_id=mint_key_certificates[denomination].data.mint_key.id)

        self.blinds[reference] = blind
        self.blinds_private[reference] = (bf, bi)
        return payload, blind

    def unblind(self, blind_signature):
        reference = blind_signature.reference
        mk_id = self.blinds[reference].mint_key_id
        mkc = self.mkc[mk_id]
        mk_pub = mkc.public_key
        bsignature = blind_signature.blind_signature
        signature = oc_crypto.unblind(bsignature, self.blinds_private[reference][1], mk_pub)
        validated = oc_crypto.decrypt(signature, mk_pub) == self.payloads[reference].hash()
        if not validated:
            raise Exception('unblinded invalid signature')
        coin = create(containers.Coin,
                      payload=self.payloads[reference].data,
                      signature=signature,
                      )
        self.coins[reference] = coin
        return coin


def validate_coin(wallet_holder, coin):
    mk_id = coin.payload.mint_key_id
    mkc = wallet_holder.mkc[mk_id]
    mk_pub = mkc.public_key
    return oc_crypto.decrypt(coin.signature, mk_pub) == containers.Payload(data=coin.payload).hash()

message_id = count(start=100000)

artifacts_dir = 'docs/artifacts'

os.makedirs(artifacts_dir, exist_ok=True)
for f in os.listdir(artifacts_dir):
    os.remove(os.path.join(artifacts_dir, f))


def write(document, name):

    if '.' not in name:
        name+='.json'

    if isinstance(document, containers.Container):
        document = document.dumps(2)
    elif type(document) in [dict,AttrDict]:
        document = dict(document)
        document = json.dumps(document, indent=2)

    with open(os.path.join(artifacts_dir, name), 'w') as f:
        f.write(document)


def create(containerclass, **kwargs):
    kwargs['_add_type'] = True
    c = containerclass(**kwargs)
    # name = c.data.type.replace(' ','_')
    # write(c, name)
    return c


issuer = DummyIssuer()
alice = DummyWallet()
bob = DummyWallet()

cipher_suite = f'{cipher_name}{key_length}-{hasher.upper()}-CHAUM86'
print(cipher_suite)

(issuer_public, issuer_secret) = oc_crypto.newkeys(key_length)
secret_issuer_key = dict(d=hex(issuer_secret.d)[2:], n=hex(issuer_secret.n)[2:])
write(secret_issuer_key, f'issuer_secret.json')


now = datetime.datetime.now()

cdd = create(containers.CDD,
             protocol_version="https://opencoin.org/1.0",
             cdd_location="https://opencent.org",
             issuer_cipher_suite=cipher_suite,
             issuer_public_master_key=dict(modulus=issuer_public.n,
                                           public_exponent=issuer_public.e,
                                           type="rsa public key"),
             cdd_serial=1,
             cdd_signing_date=now,
             cdd_expiry_date=now + datetime.timedelta(days=365),
             currency_name="OpenCent",
             currency_divisor=100,
             info_service=[[10, "https://opencent.org"]],
             mint_service=[[10, "https://opencent.org"],
                                 [20, "https://opencent.com/validate"]],
             renew_service=[[10, "https://opencent.org"]],
             redeem_service=[[10, "https://opencent.org"]],
             denominations=[1, 2, 5],
             additional_info="")
cdd.set_id("issuer_public_master_key")
write(cdd,'cdd.json')

master_key = containers.PublicKey(data=cdd.issuer_public_master_key)
write(master_key, 'issuer_public_master_key.json')


cddc = containers.CDDC(document_data=cdd)
cddc.sign(issuer_secret)

issuer.cddcs[cddc.data.cdd.cdd_serial] = cddc

write(cddc, 'cddc')

mint_keys = {}
mint_keys_by_id = {}
mint_key_certificates = {}
for d in cdd.data.denominations:
    (public, secret) = oc_crypto.newkeys(key_length)
    mint_keys[d] = (public, secret)
    secret_mint_key = dict(d=hex(secret.d)[2:],n=hex(secret.n)[2:])
    write(secret_mint_key,f'mintkey_{d}_secret.json')

    mk = create(containers.MintKey,
                issuer_id=cdd.data.id,
                cdd_serial=cdd.data.cdd_serial,
                public_mint_key=dict(modulus=public.n,
                                     public_exponent=public.e,
                                     type="rsa public key"),
                denomination=d,
                sign_coins_not_before=now,
                sign_coins_not_after=now + datetime.timedelta(days=365),
                coins_expiry_date=now + datetime.timedelta(days=365 + 100))
    mk.set_id('public_mint_key')
    mkc = containers.MKC(document_data=mk)
    mkc.sign(issuer_secret)
    write(mk,f'mintkey_{d}.json')

    mint_key_certificates[d] = mkc

    mkc_id = mkc.data.mint_key.id

    issuer.mkc[mkc_id] = mkc
    issuer.mkc_private[mkc_id] = (public, secret)

    write(mkc, f'mkc_{d}')

# Clients fetch cddc serial and cddcs

request_cddc_serial = create(containers.RequestCDDCSerial,
                             message_reference=next(message_id))
write(request_cddc_serial, 'request_cddc_serial')

response_cddc_serial = create(containers.ResponseCDDCSerial,
                              message_reference=request_cddc_serial.message_reference,
                              cdd_serial=1)
write(response_cddc_serial, 'response_cddc_serial')

request_cddc = create(containers.RequestCDDC,
                      message_reference=next(message_id),
                      cdd_serial=response_cddc_serial.data.cdd_serial)
write(request_cddc, 'request_cddc')

response_cddc = create(containers.ResponseCDDC,
                       message_reference=request_cddc.message_reference,
                       cddc=cddc.data)
write(response_cddc, 'response_cddc')

cddc_client = containers.CDDC(data=response_cddc.cddc)
alice.cddcs[cddc_client.cdd.cdd_serial] = cddc_client
bob.cddcs[cddc_client.cdd.cdd_serial] = cddc_client

# clients fetch all mint keys

request_mint_key_certificates = create(containers.RequestMKCs,
                                       message_reference=next(message_id),
                                       mint_key_ids=[],
                                       denominations=cddc_client.cdd.denominations)
write(request_mint_key_certificates, 'request_mkc')

response_mint_key_certificates = create(containers.ResponseMKCs,
                                        message_reference=request_mint_key_certificates.message_reference,
                                        keys=[mkc.data for mkc in issuer.mkc.values()])
write(response_mint_key_certificates, 'response_mkc')

for mkc_data in response_mint_key_certificates.keys:
    mkc = containers.MKC(data=mkc_data)
    alice.add_mkc(mkc)
    bob.add_mkc(mkc)

payloads = {}
blinds = {}

# Alice prepares some blinds

for i, denomination in enumerate(cdd.denominations):
    reference = f'a{i}'
    payload, blind = alice.prepare_blind(reference, denomination)
    write(payload, f'payload_{reference}')
    write(blind, f'blind_{reference}')

request_minting = create(containers.RequestMint,
                         message_reference=next(message_id),
                         transaction_reference=oc_crypto.getrandbits(rand_length),
                         blinds=[blind.data for blind in alice.blinds.values()])
write(request_minting, 'request_mint')

# we are on the issuer side now, leaving out the transport
blind_signatures = []
for blind in alice.blinds.values():
    blind_signature = issuer.sign(blind)
    blind_signatures.append(blind_signature)
    write(blind_signature, f"blind_signature_{blind_signature.reference}")

response_minting = create(containers.ResponseMint,
                          message_reference=request_minting.message_reference,
                          blind_signatures=[blind_signature.data for blind_signature in blind_signatures])
write(response_minting, 'response_mint_a')

# back to the client side
for blind_signature in response_minting.blind_signatures:
    reference = blind_signature.reference
    coin = alice.unblind(blind_signature)

    # just for show
    print(f'validated coin {reference}:', validate_coin(alice, coin))

    write(coin, f"coin_{reference}")

# alice hands it over to bob
coinstack = create(containers.CoinStack,
                   subject="a little gift",
                   coins=[coin.data for coin in alice.coins.values()])
write(coinstack, 'coinstack')

# she deletes all traces of those coins - she is honest
for reference in list(alice.coins.keys()):
    del alice.coins[reference]
    del alice.blinds[reference]
    del alice.blinds_private[reference]

denomination = 2
# Bob needs to renew the coins. He wants some 2 opencent coins.
for i in range(4):
    reference = f'b{i}'
    payload, blind = bob.prepare_blind(reference, denomination)
    write(payload, f'payload_{reference}')
    write(blind, f'blind_{reference}')

request_renewal = create(containers.RequestRenew,
                         message_reference=next(message_id),
                         transaction_reference=oc_crypto.getrandbits(rand_length),
                         coins=coinstack.coins,
                         blinds=[blind.data for blind in bob.blinds.values()]
                         )
write(request_renewal, 'request_renew')


# the issuer is on a break, let's signal that

response_delay = create(containers.ResponseDelay,
                        message_reference = request_renewal.message_reference,
                        status_code=300)
write(response_delay, 'response_delay')


# bob waits, then asks to resume

request_resume=create(containers.RequestResume,
                      message_reference=next(message_id),
                      transaction_reference=request_renewal.transaction_reference)
write(request_resume, 'request_resume')

# does the sum for coins and blinds match?
assert(request_resume.transaction_reference == request_renewal.transaction_reference)
coin_sum = sum(coin.payload.denomination for coin in request_renewal.coins)
assert (coin_sum == issuer.sum_blinds(request_renewal.blinds))

print(f'renew coins worth {coin_sum}')

blind_signatures = []
for blind in request_renewal.blinds:
    blind_signature = issuer.sign(blind)
    blind_signatures.append(blind_signature)
    write(blind_signature, f"blind_signature_{blind_signature.reference}")

response_minting = create(containers.ResponseMint,
                          message_reference=request_renewal.message_reference,
                          blind_signatures=blind_signatures)
write(response_minting, 'response_mint_b')

# back to bob, who unblinds the signatures
for blind_signature in response_minting.blind_signatures:
    reference = blind_signature.reference
    coin = bob.unblind(blind_signature)

    # just for show
    print(f'validated coin {reference}:', validate_coin(bob, coin))

    write(coin, f"coin_{reference}")


# bob wants to redeem the first two coins

request_redeeming = create(containers.RequestRedeem,
                           message_reference=next(message_id),
                           coins=list(list(bob.coins.values())[:2]))

write(request_redeeming, 'request_redeem')


# the issuer checks the coins

assert(all(validate_coin(issuer,coin) for coin in request_renewal.coins))

response_redeeming = create(containers.ResponseRedeem,
                             message_reference = request_redeeming.message_reference
                             )
write(response_redeeming, 'response_redeem')

import schemata, json
write(json.dumps(schemata.all_json_schema_dict(), indent=2), 'all_schemata.json')