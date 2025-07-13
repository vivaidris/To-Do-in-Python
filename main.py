import tkinter as tk
import LoginFrame
import MainMenuFrame
import SignupFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do App")
        self.geometry("400x300")
        self.frames = {}

        self.show_signup()

    def show_signup(self):
        from SignupFrame import SignupFrame
        frame = SignupFrame(self, self.show_main_menu)
        frame.pack(fill="both", expand=True)
        self._swap_frame(frame)

    def show_main_menu(self, username):
        from MainMenuFrame import MainMenuFrame  # once it exists
        frame = MainMenuFrame(self, username)
        frame.pack(fill="both", expand=True)
        self._swap_frame(frame)

    def _swap_frame(self, new_frame):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
