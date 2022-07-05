import datetime

import os

import oc_crypto
import containers

os.makedirs('artifacts', exist_ok=True)

def write(document, name):

    if isinstance(document, containers.Container):
        document = document.dumps()

    with open(os.path.join('artifacts', name), 'w') as f:
        f.write(document)



(issuer_public, issuer_secret) = oc_crypto.newkeys(512)
now = datetime.datetime.now()

cdd_data = dict(protocol_version="http://opencoin.org/1.0",
                cdd_location="http://opencent.org",
                issuer_cipher_suite="RSA-SHA512-CHAUM86",
                issuer_public_master_key=dict(modulus=issuer_public.n,
                                              public_exponent=issuer_public.e,
                                              type="rsa public key"),
                cdd_serial=1,
                cdd_signing_date=now,
                cdd_expiry_date=now + datetime.timedelta(days=365),
                currency_name="OpenCent",
                currency_divisor=100,
                info_service=[[10, "http://opencent.org"]],
                validation_service=[[10, "http://opencent.org"],
                                    [20, "http://opencent.com/validate"]],
                renewal_service=[[10, "http://opencent.org"]],
                invalidation_service=[[10, "http://opencent.org"]],
                denominations=[1, 2, 5],
                additional_info="",
                type="cdd")

cdd = containers.CDD(cdd_data)
cdd.set_id("issuer_public_master_key")

cddc = containers.CDDC(document_data=cdd)
cddc.sign(issuer_secret)

write(cddc, 'cddc.oc')

mint_keys = {}
mint_keys_by_id = {}
mint_key_certificates = {}
for d in cdd.data.denominations:
    (public, secret) = oc_crypto.newkeys(512)
    mint_keys[d] = (public, secret)

    mint_key_data = dict(issuer_id=cdd.data.id,
                         cdd_serial=cdd.data.cdd_serial,
                         public_mint_key=dict(modulus=public.n,
                                              public_exponent=public.e,
                                              type="rsa public key"),
                         denomination=d,
                         sign_coins_not_before=now,
                         sign_coins_not_after=now + datetime.timedelta(days=365),
                         coins_expiry_date=now + datetime.timedelta(days=365 + 100),
                         type="mint key")

    mk = containers.MintKey(mint_key_data)
    mk.set_id('public_mint_key')
    mint_key_certificate = containers.MintKeyCertificate(document_data=mk)
    mint_key_certificate.sign(issuer_secret)

    mint_key_certificates[d] = mint_key_certificate
    write(mint_key_certificate, f'mkc_{d}.oc')

payloads = {}
blinds = {}
for i, d in enumerate(cdd.data.denominations):
    serial = oc_crypto.read_random_odd_int(256)
    payload_data = dict(protocol_version="http://opencoin.org/1.0",
                        issuer_id=cdd.data.id,
                        cdd_location="http://opencent.org",
                        denomination=d,
                        mint_key_id=mint_key_certificates[d].data.mint_key.id,
                        serial=serial,
                        type="payload")
    payload = containers.Payload(payload_data)
    payloads[i] = payload
    write(payload, f'payload_{i}.oc')

    mk_public, mk_secret = mint_keys[d]

    bf, bi = oc_crypto.get_blinding_factors(mk_public)
    blinded = oc_crypto.blind_message(payload.hash(), bf, mk_public)
    blind = containers.Blind(dict(reference=f"r_{i}",
                       blinded_payload_hash=blinded,
                       mint_key_id=mint_key_certificates[d].data.mint_key.id,
                       type="blinded payload hash"
                       )
                  )
    blinds[i] = (d, bf, bi, blind)
    write(blind, f'blind_{i}.oc')

# we are on the issuer side now, leaving out the transport
blind_signatures = {}
for i, (d,_,_,blind) in blinds.items():
    bsignature = oc_crypto.sign_blind(blind.data.blinded_payload_hash,
                                      mint_keys[d][1])
    blind_signature = containers.BlindSignature(dict(blind_signature=bsignature,
                                          reference=blind.data.reference,
                                          type="blind signature"))
    blind_signatures[i]=blind_signature
    write(blind_signature,f"blind_signature_{i}.oc")


# back to the client side
for i, (d,bf, bi, blind) in blinds.items():
    mk_pub = mint_keys[d][0]
    bsignature = blind_signatures[i].data.blind_signature
    signature = oc_crypto.unblind(bsignature, bi, mk_pub)
    validated = oc_crypto.decrypt(signature, mk_pub) == payloads[i].hash()
    print(f'validated coin {i}:', validated)
    coin = containers.Coin(dict(
            payload=payloads[i].data,
            signature=signature,
            type="coin"
    ))
    write(coin,f"coin_{i}.oc")
