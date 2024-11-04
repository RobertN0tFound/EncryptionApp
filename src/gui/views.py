import tkinter as tk
from tkinter import filedialog, messagebox

class MainMenuView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose an operation:").pack(pady=10)

        # Button to select encryption
        tk.Button(self, text="Encrypt", command=self.controller.on_encrypt_selected).pack(pady=5)

        # Button to select decryption
        tk.Button(self, text="Decrypt", command=self.controller.on_decrypt_selected).pack(pady=5)


class DecryptMenuView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose decryption option:").pack(pady=10)

        # Button to select text decryption
        tk.Button(self, text="Decrypt Text", command=self.controller.on_text_decrypt_selected).pack(pady=5)

        # Button to select file decryption
        tk.Button(self, text="Decrypt File", command=self.controller.on_file_decrypt_selected).pack(pady=5)


class TextEncryptView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Algorithm:").pack(pady=5)

        # Dropdown menu for selecting algorithm
        self.algorithm_var = tk.StringVar(value="RSA")
        tk.OptionMenu(self, self.algorithm_var, "RSA", "Knapsack", "ElGamal").pack(pady=5)

        tk.Label(self, text="Enter Plaintext:").pack(pady=5)

        # Text field for plaintext input
        self.plaintext_entry = tk.Entry(self, width=40)
        self.plaintext_entry.pack(pady=5)

        # Encrypt button
        tk.Button(self, text="Encrypt", command=self.encrypt_text).pack(pady=10)

    def encrypt_text(self):
        algorithm = self.algorithm_var.get()
        plaintext = self.plaintext_entry.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt.")
            return
        result = self.controller.encrypt_text(algorithm, plaintext)
        messagebox.showinfo("Encryption Result", result)


class FileEncryptView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Algorithm:").pack(pady=5)

        # Dropdown menu for selecting algorithm
        self.algorithm_var = tk.StringVar(value="RSA")
        tk.OptionMenu(self, self.algorithm_var, "RSA", "Knapsack", "ElGamal").pack(pady=5)

        tk.Label(self, text="Select a File:").pack(pady=5)

        self.filepath_entry = tk.Entry(self, width=40)
        self.filepath_entry.pack(pady=5)

        tk.Button(self, text="Browse", command=self.browse_file).pack(pady=5)

        # Encrypt button
        tk.Button(self, text="Encrypt File", command=self.encrypt_file).pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.filepath_entry.delete(0, tk.END)
            self.filepath_entry.insert(0, file_path)

    def encrypt_file(self):
        algorithm = self.algorithm_var.get()
        file_path = self.filepath_entry.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to encrypt.")
            return
        result = self.controller.encrypt_file(algorithm, file_path)
        messagebox.showinfo("Encryption Result", result)


class TextDecryptView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Decryption Algorithm:").pack(pady=5)

        # Dropdown menu for selecting algorithm
        self.algorithm_var = tk.StringVar(value="RSA")
        tk.OptionMenu(self, self.algorithm_var, "RSA", "Knapsack", "ElGamal").pack(pady=5)

        tk.Label(self, text="Enter Encrypted Text:").pack(pady=5)

        # Text field for encrypted text input
        self.encrypted_entry = tk.Entry(self, width=40)
        self.encrypted_entry.pack(pady=5)

        # Decrypt button
        tk.Button(self, text="Decrypt", command=self.decrypt_text).pack(pady=10)

    def decrypt_text(self):
        algorithm = self.algorithm_var.get()
        encrypted_text = self.encrypted_entry.get()
        if not encrypted_text:
            messagebox.showerror("Error", "Please enter text to decrypt.")
            return
        result = self.controller.decrypt_text(algorithm, encrypted_text)
        messagebox.showinfo("Decryption Result", result)


class FileDecryptView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select Decryption Algorithm:").pack(pady=5)

        # Dropdown menu for selecting algorithm
        self.algorithm_var = tk.StringVar(value="RSA")
        tk.OptionMenu(self, self.algorithm_var, "RSA", "Knapsack", "ElGamal").pack(pady=5)

        tk.Label(self, text="Select a File:").pack(pady=5)

        self.filepath_entry = tk.Entry(self, width=40)
        self.filepath_entry.pack(pady=5)

        tk.Button(self, text="Browse", command=self.browse_file).pack(pady=5)

        # Decrypt button
        tk.Button(self, text="Decrypt File", command=self.decrypt_file).pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.filepath_entry.delete(0, tk.END)
            self.filepath_entry.insert(0, file_path)

    def decrypt_file(self):
        algorithm = self.algorithm_var.get()
        file_path = self.filepath_entry.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to decrypt.")
            return
        result = self.controller.decrypt_file(algorithm, file_path)
        messagebox.showinfo("Decryption Result", result)
