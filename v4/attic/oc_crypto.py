# This file is here only for historic purposes

from rsa_oc import get_blinding_factors, blind, unblind, sign, verify, generate_keys, getrandbits


class PublicKey:

    def __init__(self, modulus, public_exponent):
        self.n = modulus
        self.e = public_exponent


def blind_message(message, bf, pub):
    return blind(message, bf, pub)


def sign_blind(blinded, priv):
    return sign(blinded, priv)


def decrypt(message, pub):
    return verify(message, pub)


def newkeys(bits):
    return generate_keys(bits)


def sign_container(container, priv):
    return sign(container.hash(), priv)


if __name__ == '__main__':
    pub, priv = newkeys(256)

    serial = getrandbits(128)

    print('serial   ', serial)
    print()

    bf, bi = get_blinding_factors(pub)
    print('bf       ', bf)
    print('bi       ', bi)
    print()

    blinded = blind_message(serial, bf, pub)
    print('blinded  ', blinded)

    blind_signature = sign_blind(blinded, priv)
    print()
    print('blind_sig', blind_signature)
    print()
    signature = unblind(blind_signature, bi, pub)
    print('signature', signature)
    decrypted = decrypt(signature, pub)
    print()
    print('decrypted', decrypted)
    print()
    print('matches  ', decrypted == serial)
