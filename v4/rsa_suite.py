"""
Demo implementation of a cipher suite for documentation purposes only.

Layer on top of cryptography.io, but also adds blinding support.
"""
import math
import random  # this is insecure, but doesn't matter for documentation

import cryptography.exceptions
from cryptography.hazmat.backends.openssl.backend import Backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


class Suite:
    """
    Represents an RSA cipher suite.

    Used to work towards a shared interface
    """

    def __init__(self, key_length=2048, hash_alg="SHA256", random_length=128):
        self.key_length = key_length
        self.hash_alg = hash_alg
        self.random_length = random_length

    def get_hasher(self):
        """Returns the configured hash algorithm"""

        return getattr(hashes, self.hash_alg)()

    def generate_keys(self, key_length=None):
        """Generate public, private keys"""
        if key_length is None:
            key_length = self.key_length
        private = PrivateKey(rsa.generate_private_key(65537, key_length), self)
        return private.pubkey, private

    def get_random_bits(self, length=None):
        """Random bits, here only pseudo random. Shortcut to have uniform length"""
        if length is None:
            length = self.random_length
        return random.getrandbits(length)

    def get_random_bytes(self, length):
        """Random bytes"""
        return random.randbytes(length)

    def get_padding(self):
        """Returns the padding mechanism"""
        return padding.PSS(mgf=padding.MGF1(self.get_hasher()),
                           salt_length=padding.PSS.MAX_LENGTH)

    def name(self):
        """Returns the string describing the suite as configured"""
        return f"RSA-{self.hash_alg}-PSS-CHAUM82"

    def restore_public_key(self, e, n):
        """Needed to create a public key from JSON

        We don't need an equivalent for private keys, because they are never
        transferred.
        """
        public_numbers = rsa.RSAPublicNumbers(e, n)
        backend = Backend()
        return PubKey(backend.load_rsa_public_numbers(public_numbers), self)


class PrivateKey:

    def __init__(self, private_key: rsa.RSAPrivateKey, suite: Suite):
        self.private_key = private_key
        private_numbers = private_key.private_numbers()
        self.d = private_numbers.d
        self.p = private_numbers.p
        self.q = private_numbers.q

        self.public_key = private_key.public_key()
        self.pubkey = PubKey(self.public_key, suite)
        self.n = self.pubkey.n
        self.suite = suite

    def sign_blind(self, blind: int):
        """raw RSA sign, without padding"""
        return pow(blind, self.d, self.n)

    def sign(self, message):
        """Proper RSA padded signature"""

        if type(message) == str:
            message = message.encode('utf-8')

        return self.private_key.sign(
                message,
                self.suite.get_padding(),
                self.suite.get_hasher())


class PubKey:
    def __init__(self, public_key: rsa.RSAPublicKey, suite):
        self.public_key = public_key
        public_numbers = public_key.public_numbers()
        self.n = public_numbers.n
        self.e = public_numbers.e
        self.suite = suite

    def blinding_factors(self):
        """Return blinder, unblinder"""
        while 1:
            unblinder = self.suite.get_random_bits(self.suite.random_length)
            if math.gcd(unblinder, self.n) == 1:  # relative prime
                break
        blinder = pow(rsa._modinv(unblinder, self.n), self.e, self.n)
        return blinder, unblinder

    def _blinding_operation(self, m, secret, n):
        return (m * secret) % n

    def blind(self, m: int, secret: int):
        """Blind a message with a secret"""
        return self._blinding_operation(m, secret, self.n)

    def unblind(self, m: int, secret: int):
        """Unblind a message using a secret"""
        return self._blinding_operation(m, secret, self.n)

    def verify(self, signature, message):
        """Proper RSA padded signature verification"""

        if type(message) == str:
            message = message.encode('utf-8')
        try:
            self.public_key.verify(
                    signature,
                    message,
                    self.suite.get_padding(),
                    self.suite.get_hasher())
        except cryptography.exceptions.InvalidSignature:
            return False
        return True

    def verify_blind(self, signature: int, message: int):
        """Verify the signature on a coin"""
        verified = pow(signature, self.e, self.n)
        return verified == message


if __name__ == '__main__':
    random.seed(1)
    suite = Suite(key_length=512)
    print(suite.name())
    public, private = suite.generate_keys()

    serial = suite.get_random_bits()
    print(serial)
    bf, bi = public.blinding_factors()

    blinded = public.blind(serial, bf)

    blind_signature = private.sign_blind(blinded)

    unblinded = public.unblind(blind_signature, bi)

    print(public.verify_blind(unblinded, serial))

    text = 'my message'
    signature = private.sign(text)
    print(int.from_bytes(signature, 'big'))
    print(public.verify(signature, text))
