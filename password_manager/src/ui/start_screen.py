from tkinter import Tk, ttk, constants

class StartScreen:
    def __init__(self, root):
        self.root = root

    def start_screen(self):
        start_label = ttk.Label(self.root, text="Log in or create user")
        start_label.grid(row=0, column=0, columnspan=2)

        login_button = ttk.Button(self.root, text="Log in")
        login_button.grid(row=2, column=0)

        create_user_button = ttk.Button(self.root, text="Create user")
        create_user_button.grid(row=2, column=1)

        generate_password_button = ttk.Button(self.root, text="Generate Password")
        generate_password_button.grid(row=3, column=0, columnspan=2)


window = Tk()
#window.geometry("600x400")
window.title("Password Manager")
startscreen = StartScreen(window)
startscreen.start_screen()
window.mainloop()