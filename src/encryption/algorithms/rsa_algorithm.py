import random
from encryption.algorithms.base_algorithm import BaseAlgorithm
from math import gcd

class RSAAlgorithm(BaseAlgorithm):
    def __init__(self, key_size=2048):
        self.public_key, self.private_key = self.generate_rsa_keys(key_size)

    def generate_prime(self, bits):
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        while not all(candidate % i != 0 for i in range(2, int(candidate ** 0.5) + 1)):
            candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        return candidate

    def generate_rsa_keys(self, bits=1024):
        p = self.generate_prime(bits // 2)
        q = self.generate_prime(bits // 2)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        d = pow(e, -1, phi)
        return (n, e), (n, d)

    def encrypt(self, message):
        n, e = self.public_key
        return pow(message, e, n)

    def decrypt(self, ciphertext):
        n, d = self.private_key
        return pow(ciphertext, d, n)