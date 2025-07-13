# MainMenuFrame.py

import tkinter as tk

class MainMenuFrame(tk.Frame):
    def __init__(self, master, app, username):
        super().__init__(master)
        self.app = app
        self.username = username

        self.create_widgets()

    def create_widgets(self):
        # Welcome message
        tk.Label(self, text=f"Welcome, {self.username}!", font=('Arial', 16)).pack(pady=10)

        # Buttons for menu actions
        tk.Button(self, text="Create New List", command=self.create_list).pack(fill='x', padx=50, pady=5)
        tk.Button(self, text="View/Edit Lists", command=self.view_lists).pack(fill='x', padx=50, pady=5)
        tk.Button(self, text="Delete List", command=self.delete_list).pack(fill='x', padx=50, pady=5)
        tk.Button(self, text="Settings", command=self.open_settings).pack(fill='x', padx=50, pady=5)
        tk.Button(self, text="Logout", command=self.logout).pack(fill='x', padx=50, pady=5)

    # Placeholder methods for button commands
    def create_list(self):
        print("Create List clicked")

    def view_lists(self):
        print("View/Edit Lists clicked")

    def delete_list(self):
        print("Delete List clicked")

    def open_settings(self):
        print("Settings clicked (not yet implemented)")

    def logout(self):
        self.app.show_frame("LoginFrame")  # Or wherever you route your login screen
