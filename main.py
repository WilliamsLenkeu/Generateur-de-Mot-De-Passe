import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Générateur de Mots de Passe")

        self.length_label = tk.Label(master, text="Longueur du mot de passe:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.upper_var = tk.IntVar()
        self.upper_check = tk.Checkbutton(master, text="Lettres majuscules", variable=self.upper_var)
        self.upper_check.pack()

        self.lower_var = tk.IntVar()
        self.lower_check = tk.Checkbutton(master, text="Lettres minuscules", variable=self.lower_var)
        self.lower_check.pack()

        self.digit_var = tk.IntVar()
        self.digit_check = tk.Checkbutton(master, text="Chiffres", variable=self.digit_var)
        self.digit_check.pack()

        self.special_var = tk.IntVar()
        self.special_check = tk.Checkbutton(master, text="Caractères spéciaux", variable=self.special_var)
        self.special_check.pack()

        self.generate_button = tk.Button(master, text="Générer le mot de passe", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une longueur valide.")
            return

        if length <= 0:
            messagebox.showerror("Erreur", "La longueur du mot de passe doit être supérieure à zéro.")
            return

        chars = ""
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.digit_var.get():
            chars += string.digits
        if self.special_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins un type de caractère.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        messagebox.showinfo("Mot de Passe Généré", f"Votre mot de passe sécurisé est:\n{password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
