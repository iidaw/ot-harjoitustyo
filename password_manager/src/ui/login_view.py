from tkinter import ttk, StringVar, constants
from entities.user import User
#from ui.add_passwords_view import AddPasswordView


class LoginView:
    def __init__(self, root, handle_create_user, handle_login, show_start_view):
        self.root = root
        self.handle_create_user = handle_create_user
        self.handle_login = handle_login
        self.show_start_view = show_start_view
        self.frame = None

        self.initialize()

    def pack(self):
        if self.frame:
            self.frame.pack(fill=constants.X)

    def destroy(self):
        if self.frame:
            self.frame.destroy()

   # def handel_login(self):
    #    username = self.username_entry.get()
     #   password = self.password_entry.get()

        # toiminnallisuus muualta

    def initialize(self):
        print(self.root)
        self.frame = ttk.Frame(master=self.root)

        self.username_entry_var = StringVar()
        self.username_entry_var.set("")

        self.password_entry_var = StringVar()
        self.password_entry_var.set("")

        label = ttk.Label(master=self.frame,
                          text="Username and password to login")
        label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(master=self.frame, text="Username:")
        username_label.grid(row=2, column=0, sticky=constants.W)

        username_entry = ttk.Entry(
            master=self.frame, textvariable=self.username_entry_var)
        username_entry.grid(row=3, column=0, columnspan=2, sticky=constants.EW)

        password_label = ttk.Label(master=self.frame, text="Password:")
        password_label.grid(row=4, column=0, sticky=constants.W)

        password_entry = ttk.Entry(
            master=self.frame, textvariable=self.password_entry_var)
        password_entry.grid(row=5, column=0, columnspan=2, sticky=constants.EW)

        login_button = ttk.Button(
            master=self.frame, text="Login")  # lisää command
        login_button.grid(row=6, column=0, columnspan=2, sticky=constants.EW)

        back_button = ttk.Button(
            master=self.frame, text="Back", command=self.show_start_view)  # lisää command
        back_button.grid(row=7, column=0, sticky=constants.EW)

    # def login(self):
     #   if self.username_entry_var and self.password_entry_var:
      #      given_username = self.username_entry.get()
       #     given_password = self.password_entry.get()
        #    #print(given_username, given_password)
        #   user = User(given_username, given_password)
        #  if user.login():

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
