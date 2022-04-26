from tkinter import ttk, constants
from entities.user import User
from service.service import Service
#from ui.add_passwords_view import AddPasswordView


class LoginView:
    def __init__(self, root, handle_create_user, handle_login, show_start_view, service: Service):
        self.root = root
        self.handle_create_user = handle_create_user
        self.handle_login = handle_login
        self.show_start_view = show_start_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.service = service

        self.initialize()

    def pack(self):
        if self.frame:
            self.frame.pack(fill=constants.X)

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.service.login(username, password)
        self.handle_login()

        # toimii ehkä

    def initialize(self):
        # print(self.root) testausta varten
        self.frame = ttk.Frame(master=self.root)

        label = ttk.Label(master=self.frame,
                          text="Username and password to login")
        label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self.frame, text="Username:")
        username_label.grid(row=2, column=0, sticky=constants.W)

        self.username_entry = ttk.Entry(
            master=self.frame)
        self.username_entry.grid(
            row=3, column=0, columnspan=2, sticky=constants.EW)

        password_label = ttk.Label(master=self.frame, text="Password:")
        password_label.grid(row=4, column=0, sticky=constants.W)

        self.password_entry = ttk.Entry(
            master=self.frame)
        self.password_entry.grid(
            row=5, column=0, columnspan=2, sticky=constants.EW)

        login_button = ttk.Button(
            master=self.frame, text="Login", command=self.login_handler)
        login_button.grid(row=6, column=0, columnspan=2, sticky=constants.EW)

        back_button = ttk.Button(
            master=self.frame, text="Back", command=self.show_start_view)
        back_button.grid(row=7, column=0, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
