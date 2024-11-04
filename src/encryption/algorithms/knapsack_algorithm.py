import random
from encryption.algorithms.base_algorithm import BaseAlgorithm
from math import gcd

class KnapsackAlgorithm(BaseAlgorithm):
    def __init__(self, length=8):
        self.public_key, self.private_key = self.generate_knapsack_keys(length)

    def generate_superincreasing_sequence(self, length, start=2):
        w = [start]
        for _ in range(1, length):
            w.append(sum(w) + random.randint(1, 10))
        return w

    def generate_knapsack_keys(self, length=8):
        w = self.generate_superincreasing_sequence(length)
        M = sum(w) + random.randint(1, 100)
        N = random.randrange(2, M)
        while gcd(N, M) != 1:
            N = random.randrange(2, M)
        b = [(N * w_i) % M for w_i in w]
        return b, (w, M, N)

    def mod_inverse(self, e, phi):
        g, x, _ = self.extended_gcd(e, phi)
        if g != 1:
            raise ValueError("No modular inverse")
        return x % phi

    def extended_gcd(self, a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = self.extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

    def encrypt(self, message):
        b = self.public_key
        binary_message = [int(bit) for bit in bin(message)[2:]]
        binary_message = [0] * (len(b) - len(binary_message)) + binary_message
        return sum(m_i * b_i for m_i, b_i in zip(binary_message, b))

    def decrypt(self, ciphertext):
        w, M, N = self.private_key
        N_inv = self.mod_inverse(N, M)
        c_prime = (ciphertext * N_inv) % M

        message_bits = []
        for w_i in reversed(w):
            if c_prime >= w_i:
                message_bits.append(1)
                c_prime -= w_i
            else:
                message_bits.append(0)
        message_bits.reverse()
        return int(''.join(map(str, message_bits)), 2)