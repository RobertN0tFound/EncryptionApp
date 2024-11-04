from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        pass