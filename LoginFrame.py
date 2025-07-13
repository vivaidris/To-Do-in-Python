import tkinter as tk
import json
from tkinter import messagebox
import SignupFrame
from main_2 import App
import MainMenuFrame

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        tk.Button(self, text="Login", command=self.attempt_login).pack()
        tk.Button(self, text="Sign Up", command=lambda: master.show_frame(SignupFrame)).pack()

    def attempt_login(self):
        user = self.username.get()
        pwd = self.password.get()
        try:
            with open("json_files/users.json", "r") as f:
                data = json.load(f)
            if data.get("username") == user and data.get("password") == pwd:
                messagebox.showinfo("Success", "Logged in!")
                self.master.show_frame(MainMenuFrame)
            else:
                messagebox.showerror("Failed", "Invalid credentials")
        except FileNotFoundError:
            messagebox.showerror("Error", "User file not found.")

if __name__ == "__main__":
    app = App()
    app.mainloop()