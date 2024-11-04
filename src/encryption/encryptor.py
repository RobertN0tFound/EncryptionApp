from encryption.algorithms import RSAAlgorithm, KnapsackAlgorithm, ElGamalAlgorithm

class Encryptor:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def encrypt(self, message):
        return self.algorithm.encrypt(message)