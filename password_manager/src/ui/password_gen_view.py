from tkinter import END, ttk, constants
#import string
#import random
from service.password_generator import password_generator


class PasswordGeneratorView:
    def __init__(self, root, show_add_password_view):
        self.root = root
        self.frame = None
        #self.show_start_view = show_start_view
        self.password_entry = None
        self.length_entry = None
        self.final_password = str
        self.show_add_password_view = show_add_password_view

        self.init_frame()

    def pack(self):
        """Näyttää näkymän"""
        self.frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self.frame.destroy()

    def password_gen(self):
        length_label = ttk.Label(
            master=self.frame, text="Enter length (number):")
        length_label.grid(row=0, column=0, columnspan=2, sticky=constants.EW)

        self.length_entry = ttk.Entry(master=self.frame)
        self.length_entry.grid(
            row=1, column=0, sticky=constants.EW)

        generated_pw_label = ttk.Label(
            master=self.frame, text="Generated password:")
        generated_pw_label.grid(row=2, column=0, sticky=constants.W)

        self.password_entry = ttk.Entry(master=self.frame, text="")
        self.password_entry.grid(
            row=3, column=0, columnspan=2, sticky=constants.EW)

        generate_button = ttk.Button(
            master=self.frame, text="Generate", command=self.generate_password)
        generate_button.grid(
            row=4, column=0, columnspan=2, sticky=constants.EW)

        back_button = ttk.Button(
            master=self.frame, text="Back", command=self.show_add_password_view)
        back_button.grid(row=5, column=0, sticky=constants.EW)

        empty_label = ttk.Label(master=self.frame)
        empty_label.grid(row=6, column=0)

    def init_frame(self):
        """Vastaa näkymän asettelusta
        """

        self.frame = ttk.Frame(master=self.root)

        self.password_gen()

        self.frame.grid_columnconfigure(0, weight=1, minsize=500)

    def generate_password(self):
        """Muodostaa generoidun salasanan ja palauttaa sen näkymään"""

        self.password_entry.delete(0, END)
        password_length = int(self.length_entry.get())

        self.password_entry.insert(0, password_generator(password_length))
