from encryption.algorithms import RSAAlgorithm, KnapsackAlgorithm, ElGamalAlgorithm

class Decryptor:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def decrypt(self, ciphertext):
        return self.algorithm.decrypt(ciphertext)