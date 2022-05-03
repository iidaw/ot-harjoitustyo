from tkinter import ttk, constants
from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.password_gen_view import PasswordGeneratorView


class StartScreen:
    """Luokka joka vastaa alkunäkymästä
    """

    def __init__(self, root, show_login_view, show_create_user_view, show_password_gen_view):
        """Luokan konstruktori
        """

        self.root = root
        #self.login = login
        #self.create_user = create_user
        self.frame = None
        self.show_login_view = show_login_view
        self.show_create_user_view = show_create_user_view
        #self.show_password_gen_view = show_password_gen_view
        self.show_password_gen_view = show_password_gen_view

        self.initialize()

    def pack(self):
        """Näyttää näkymän"""
        self.frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        if self.frame:
            self.frame.destroy()

    def initialize(self):
        """Vastaa näkymän asettelusta
        """

        self.frame = ttk.Frame(master=self.root)

        start_label = ttk.Label(
            master=self.frame, text="Log in or create user")
        start_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        empty_label = ttk.Label(master=self.frame, text="")
        empty_label.grid(row=2, column=0)

        login_button = ttk.Button(
            master=self.frame, text="Log in", command=self.show_login_view)
        login_button.grid(row=3, column=0, sticky=constants.EW)

        create_user_button = ttk.Button(
            master=self.frame, text="Create user", command=self.show_create_user_view)
        create_user_button.grid(row=4, column=0, sticky=constants.EW)

        generate_password_button = ttk.Button(
            master=self.frame, text="Generate Password", command=self.show_password_gen_view)
        generate_password_button.grid(
            row=5, column=0, columnspan=2, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=1, minsize=500)
