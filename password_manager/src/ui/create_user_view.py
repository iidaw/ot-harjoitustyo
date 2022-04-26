from tkinter import ttk, constants
from service.service import Service
from repositories.user_repo import UserRepo
from entities.user import User


class CreateUserView:
    def __init__(self, root, handle_login, handle_create_user, show_start_view, user_repo: UserRepo):
        self.root = root
        self.handle_login = handle_login
        self.handle_create_user = handle_create_user
        self.show_start_view = show_start_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.user_repo = user_repo

        self.initialize()

        # mihin pitäis lisätä "create table"??

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_user_handle(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.user_repo.create_user(User(username, password))

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        label = ttk.Label(master=self.frame, text="Create user")
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        username_label = ttk.Label(master=self.frame, text="Username:")
        username_label.grid(row=1, column=0, sticky=constants.W)

        self.username_entry = ttk.Entry(master=self.frame)
        self.username_entry.grid(row=2, column=0, sticky=constants.EW)

        password_label = ttk.Label(master=self.frame, text="Password")
        password_label.grid(row=3, column=0, sticky=constants.W)

        self.password_entry = ttk.Entry(master=self.frame)
        self.password_entry.grid(row=4, column=0, sticky=constants.EW)

        create_button = ttk.Button(
            master=self.frame, text="Create", command=self.create_user_handle)
        create_button.grid(row=5, column=0, sticky=constants.EW)

        # pitäiskö tulla joku ilmotus jos käyttäjä on lisätty

        back_button = ttk.Button(
            master=self.frame, text="Back", command=self.show_start_view)
        back_button.grid(row=6, column=0, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
