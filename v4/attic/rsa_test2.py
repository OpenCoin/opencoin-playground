# This doesn't work as expected. I assume because of pkcs1 signatures containing
# asn1 information and padding etc.


import hashlib
import sys

import rsa
from rsa import randnum, common, prime

pub, priv = rsa.newkeys(512)

serial = randnum.read_random_odd_int(256)


print('serial   ',serial)
print()

def blind_factor():
    for _ in range(1000):
        blind_r = rsa.randnum.randint(pub.n-1)
        if rsa.prime.are_relatively_prime(pub.n, blind_r):
            return blind_r
    raise RuntimeError("unable to find blinding factor")

def blinding_factors():
    bf = blind_factor()
    bi = rsa.common.inverse(bf, pub.n)
    return bf, bi

def blind(message, bf, pub):
    return (message * pow(bf, pub.e, pub.n)) % pub.n

def unblind(blind_message, bi, pub):
    return (bi * blind_message) % pub.n

def int2bytes(i):
    return i.to_bytes((i.bit_length() + 7) // 8, byteorder='big')

bf, bi = blinding_factors()
print('bf       ', bf)
print('bi       ', bi)
print()

blinded = blind(serial, bf, pub)
print('blinded  ', blinded)

blind_signature = int.from_bytes(rsa.pkcs1.sign(int2bytes(blinded), priv, 'SHA-256'), 'big')
print()
print('blind_sig', blind_signature)
print()
signature = unblind(blind_signature, bi, pub)
print('signature', signature)
verified = rsa.pkcs1.verify(int2bytes(serial),int2bytes(signature),pub)
print()
print('verified', verified)