import tkinter as tk
from tkinter import messagebox
import json
import os

class SignupFrame(tk.Frame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.master = master
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Create a New Account").pack(pady=10)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Confirm Password").pack()
        self.confirm_entry = tk.Entry(self, show="*")
        self.confirm_entry.pack()

        tk.Button(self, text="Sign Up", command=self.attempt_signup).pack(pady=5)
        tk.Button(self, text="Back to Login", command=self.switch_to_login).pack()

    def attempt_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        os.makedirs('json_files', exist_ok=True)
        user_data = {"username": username, "password": password}

        with open("json_files/users.json", "w") as file:
            json.dump(user_data, file, indent=4)

        messagebox.showinfo("Success", "Account created successfully!")
        self.switch_to_login()
