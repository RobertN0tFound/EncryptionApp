import tkinter as tk
from gui.views import (
    MainMenuView,
    TextEncryptView,
    FileEncryptView,
    DecryptMenuView,
    TextDecryptView,
    FileDecryptView
)
from gui.controllers import Controller
from utils.logger import Logger

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encryption Tool")
        self.geometry("400x400")

        self.logger = Logger()
        self.controller = Controller(self)
        self.show_main_menu()

    def show_main_menu(self):
        """Display the main menu for choosing to encrypt or decrypt."""
        self.clear_window()
        main_menu = MainMenuView(self, self.controller)
        main_menu.pack()

    def show_text_encrypt_view(self):
        """Display the text encryption view."""
        self.clear_window()
        text_view = TextEncryptView(self, self.controller)
        text_view.pack()

    def show_file_encrypt_view(self):
        """Display the file encryption view."""
        self.clear_window()
        file_view = FileEncryptView(self, self.controller)
        file_view.pack()

    def show_decrypt_menu_view(self):
        """Display the decryption menu."""
        self.clear_window()
        decrypt_menu = DecryptMenuView(self, self.controller)
        decrypt_menu.pack()

    def show_text_decrypt_view(self):
        """Display the text decryption view."""
        self.clear_window()
        text_decrypt_view = TextDecryptView(self, self.controller)
        text_decrypt_view.pack()

    def show_file_decrypt_view(self):
        """Display the file decryption view."""
        self.clear_window()
        file_decrypt_view = FileDecryptView(self, self.controller)
        file_decrypt_view.pack()

    def clear_window(self):
        """Clear all widgets from the current window."""
        for widget in self.winfo_children():
            widget.destroy()