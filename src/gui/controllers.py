from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor
from encryption.algorithms import RSAAlgorithm, KnapsackAlgorithm, ElGamalAlgorithm
from utils.file_handler import read_file
from utils.logger import Logger  # Import your Logger class

class Controller:
    def __init__(self, app):
        self.app = app
        self.logger = Logger().logger  # Create an instance of Logger and get the logger
        self.logger.info("Controller initialized.")

    def on_encrypt_selected(self):
        """Show the encryption menu."""
        self.logger.info("Encryption menu selected.")
        self.app.show_text_encrypt_view()

    def on_decrypt_selected(self):
        """Show the decryption menu."""
        self.logger.info("Decryption menu selected.")
        self.app.show_decrypt_menu_view()

    def on_text_decrypt_selected(self):
        """Show the text decryption view."""
        self.logger.info("Text decryption view selected.")
        self.app.show_text_decrypt_view()

    def on_file_decrypt_selected(self):
        """Show the file decryption view."""
        self.logger.info("File decryption view selected.")
        self.app.show_file_decrypt_view()

    def on_text_encrypt_selected(self):
        """Show the text encryption view."""
        self.logger.info("Text encryption view selected.")
        self.app.show_text_encrypt_view()

    def on_file_encrypt_selected(self):
        """Show the file encryption view."""
        self.logger.info("File encryption view selected.")
        self.app.show_file_encrypt_view()

    def get_algorithm_instance(self, algorithm_name):
        """Retrieve the appropriate algorithm class instance."""
        self.logger.info(f"Retrieving algorithm instance for: {algorithm_name}")
        if algorithm_name == "RSA":
            return RSAAlgorithm()
        elif algorithm_name == "Knapsack":
            return KnapsackAlgorithm()
        elif algorithm_name == "ElGamal":
            return ElGamalAlgorithm()
        else:
            self.logger.error(f"Unknown algorithm: {algorithm_name}")
            raise ValueError(f"Unknown algorithm: {algorithm_name}")

    def encrypt_text(self, algorithm_name, plaintext):
        """Encrypt a given text with the selected algorithm."""
        self.logger.info(f"Encrypting text using {algorithm_name}.")
        algorithm = self.get_algorithm_instance(algorithm_name)
        encryptor = Encryptor(algorithm)
        
        try:
            ciphertext, keys = encryptor.encrypt(int.from_bytes(plaintext.encode(), 'big'))
            self.logger.info("Text encryption successful.")
            return (
                f"Algorithm: {algorithm_name}\n"
                f"Plaintext: {plaintext}\n"
                f"Ciphertext: {ciphertext}\n"
                f"Keys: {keys}"  # Assuming encryptor returns keys
            )
        except Exception as e:
            self.logger.error(f"Error encrypting text: {e}")
            return "Encryption failed."

    def encrypt_file(self, algorithm_name, file_path):
        """Encrypt the contents of a given file with the selected algorithm."""
        self.logger.info(f"Encrypting file: {file_path} using {algorithm_name}.")
        try:
            file_contents = read_file(file_path)
            self.logger.info("File read successfully.")
        except FileNotFoundError:
            self.logger.error("File not found.")
            return "File not found."

        algorithm = self.get_algorithm_instance(algorithm_name)
        encryptor = Encryptor(algorithm)

        try:
            ciphertext, keys = encryptor.encrypt(int.from_bytes(file_contents.encode(), 'big'))
            self.logger.info("File encryption successful.")
            return (
                f"Algorithm: {algorithm_name}\n"
                f"File: {file_path}\n"
                f"Ciphertext: {ciphertext}\n"
                f"Keys: {keys}"  # Assuming encryptor returns keys
            )
        except Exception as e:
            self.logger.error(f"Error encrypting file: {e}")
            return "Encryption failed."

    def decrypt_text(self, algorithm_name, encrypted_text):
        """Decrypt a given text with the selected algorithm."""
        self.logger.info(f"Decrypting text using {algorithm_name}.")
        algorithm = self.get_algorithm_instance(algorithm_name)
        decryptor = Decryptor(algorithm)

        try:
            decrypted_plaintext, keys = decryptor.decrypt(int(encrypted_text))
            self.logger.info("Text decryption successful.")
            return (
                f"Algorithm: {algorithm_name}\n"
                f"Encrypted Text: {encrypted_text}\n"
                f"Decrypted Plaintext: {decrypted_plaintext}\n"
                f"Keys: {keys}"  # Assuming decryptor returns keys
            )
        except Exception as e:
            self.logger.error(f"Error decrypting text: {e}")
            return "Decryption failed."

    def decrypt_file(self, algorithm_name, file_path):
        """Decrypt the contents of a given file with the selected algorithm."""
        self.logger.info(f"Decrypting file: {file_path} using {algorithm_name}.")
        try:
            file_contents = read_file(file_path)
            self.logger.info("File read successfully.")
        except FileNotFoundError:
            self.logger.error("File not found.")
            return "File not found."

        algorithm = self.get_algorithm_instance(algorithm_name)
        decryptor = Decryptor(algorithm)

        try:
            decrypted_plaintext, keys = decryptor.decrypt(int(file_contents))
            self.logger.info("File decryption successful.")
            return (
                f"Algorithm: {algorithm_name}\n"
                f"File: {file_path}\n"
                f"Decrypted Plaintext: {decrypted_plaintext}\n"
                f"Keys: {keys}"  # Assuming decryptor returns keys
            )
        except Exception as e:
            self.logger.error(f"Error decrypting file: {e}")
            return "Decryption failed."
