from tkinter import ttk, constants
from repositories.info_repo import InfoRepo


class AddPasswordView:
    def __init__(self, root):
        self.root = root
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        label = ttk.Label(master=self.frame, text="Add passwordinformation")
        label.grid(row=0, column=1, columnspan=2, sticky=constants.W)

        site_label = ttk.Label(master=self.frame, text="Site/ App: ")
        site_label.grid(row=2, column=1, sticky=constants.W)

        site_entry = ttk.Entry(master=self.frame)
        site_entry.grid(row=2, column=2, sticky=constants.EW)

        username_label = ttk.Label(master=self.frame, text="Username:")
        username_label.grid(row=3, column=1, sticky=constants.W)

        username_entry = ttk.Entry(master=self.frame)
        username_entry.grid(row=3, column=2, sticky=constants.EW)

        password_label = ttk.Label(master=self.frame, text="Password:")
        password_label.grid(row=4, column=1, sticky=constants.W)

        password_entry = ttk.Entry(master=self.frame)
        password_entry.grid(row=4, column=2, sticky=constants.EW)

        add_button = ttk.Button(master=self.frame, text="Add infromation", command=InfoRepo.create_password(
            site_entry.get(), username_entry.get(), password_entry.get()))  # lisää command
        add_button.grid(row=5, column=1, sticky=constants.EW)

        #empty_label = ttk.Label(master=self.frame, text="")
        #empty_label.grid(padx=3, pady=3, sticky=constants.W)

        logout_button = ttk.Button(master=self.frame, text="Log out")
        logout_button.grid(row=7, column=1, columnspan=2, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
