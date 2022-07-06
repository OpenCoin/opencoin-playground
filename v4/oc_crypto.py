import rsa
from rsa import randnum, common, prime, sign, PublicKey, PrivateKey
from rsa.randnum import randint, read_random_odd_int


def _get_blind_factor(pub):
    for _ in range(1000):
        blind_r = randint(pub.n-1)
        if rsa.prime.are_relatively_prime(pub.n, blind_r):
            return blind_r
    raise RuntimeError("unable to find blinding factor")

def get_blinding_factors(pub):
    bf = _get_blind_factor(pub)
    bi = rsa.common.inverse(bf, pub.n)
    return bf, bi

def blind_message(message, bf, pub):
    return (message * pow(bf, pub.e, pub.n)) % pub.n

def unblind(blind_message, bi, pub):
    return (bi * blind_message) % pub.n

def sign_blind(blinded, priv):
    return rsa.pkcs1.core.encrypt_int(blinded,priv.d, priv.n)

def decrypt(message, pub):
    return rsa.pkcs1.core.decrypt_int(message, pub.e, pub.n)

def newkeys(bits):
    return rsa.newkeys(512)

if __name__ == '__main__':

    pub, priv = newkeys(512)

    serial = read_random_odd_int(256)

    print('serial   ',serial)
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

