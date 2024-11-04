import random
from encryption.algorithms.base_algorithm import BaseAlgorithm

class ElGamalAlgorithm(BaseAlgorithm):
    def __init__(self, bits=1024):
        self.public_key, self.private_key = self.generate_elgamal_keys(bits)

    def generate_prime(self, bits):
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        while not all(candidate % i != 0 for i in range(2, int(candidate ** 0.5) + 1)):
            candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        return candidate

    def find_primitive_root(self, p):
        for g in range(2, p):
            if pow(g, 2, p) != 1 and pow(g, (p - 1) // 2, p) != 1:
                return g
        raise ValueError("No primitive root found")

    def generate_elgamal_keys(self, bits=1024):
        p = self.generate_prime(bits)
        g = self.find_primitive_root(p)
        x = random.randint(2, p - 2)
        y = pow(g, x, p)
        return (p, g, y), x

    def mod_inverse(self, a, p):
        return pow(a, p - 2, p)

    def encrypt(self, message):
        p, g, y = self.public_key
        k = random.randint(1, p - 2)
        c1 = pow(g, k, p)
        c2 = (message * pow(y, k, p)) % p
        return c1, c2

    def decrypt(self, ciphertext):
        c1, c2 = ciphertext
        p, _, _ = self.public_key
        x = self.private_key
        s = pow(c1, x, p)
        s_inv = self.mod_inverse(s, p)
        return (c2 * s_inv) % p