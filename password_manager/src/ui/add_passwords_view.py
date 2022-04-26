from tkinter import ttk, constants
from repositories.info_repo import InfoRepo
from service.service import Service


# lisää ruutu, jossa näkyy kaikki tallennetut salasanat
# jossain ylhäällä vois näkyä, mikä käyttäjä käyttää ohjelmaa
# pitäis jotenki yhdistää kirjautuminen ja salasanat niin, että kirjautuu sisään --> näkyy omat salasanat


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

        label = ttk.Label(master=self.frame, text="Add information")
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        site_label = ttk.Label(master=self.frame, text="Site/ App: ")
        site_label.grid(row=2, column=0, sticky=constants.W)

        site_entry = ttk.Entry(master=self.frame)
        site_entry.grid(row=3, column=0, sticky=constants.EW)

        username_label = ttk.Label(master=self.frame, text="Username:")
        username_label.grid(row=4, column=0, sticky=constants.W)

        username_entry = ttk.Entry(master=self.frame)
        username_entry.grid(row=5, column=0, sticky=constants.EW)

        password_label = ttk.Label(master=self.frame, text="Password:")
        password_label.grid(row=6, column=0, sticky=constants.W)

        password_entry = ttk.Entry(master=self.frame)
        password_entry.grid(row=7, column=0, sticky=constants.EW)

        add_button = ttk.Button(
            master=self.frame, text="Add infromation")  # lisää command
        # , command=InfoRepo.create_password(site_entry.get(), username_entry.get(), password_entry.get())

        add_button.grid(row=8, column=0, sticky=constants.EW)

        #empty_label = ttk.Label(master=self.frame, text="")
        #empty_label.grid(padx=3, pady=3, sticky=constants.W)

        logout_button = ttk.Button(
            master=self.frame, text="Log out")  # lisää command
        logout_button.grid(row=9, column=0, columnspan=2, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)
