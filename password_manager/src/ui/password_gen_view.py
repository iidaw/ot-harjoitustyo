from tkinter import END, ttk, constants
import string
import random

#from password_generation import generate_password


class PasswordGeneratorView:
    def __init__(self, root, show_start_view):
        self.root = root
        self.frame = None
        self.show_start_view = show_start_view
        self.password_entry = None
        self.length_entry = None
        self.final_password = str

        self.init_frame()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def password_gen(self):
        length_label = ttk.Label(
            master=self.frame, text="Enter length (number):")
        length_label.grid(row=0, column=0, sticky=constants.W)

        self.length_entry = ttk.Entry(master=self.frame)
        self.length_entry.grid(
            row=1, column=0, columnspan=2, sticky=constants.EW)

        generated_pw_label = ttk.Label(
            master=self.frame, text="Generated password:")
        generated_pw_label.grid(row=2, column=0, sticky=constants.W)

        self.password_entry = ttk.Entry(master=self.frame, text="")
        self.password_entry.grid(
            row=3, column=0, columnspan=2, sticky=constants.EW)

        # lisää command, miten saa yhdistettyä generate funktion??
        generate_button = ttk.Button(
            master=self.frame, text="Generate", command=self.generate_password)
        generate_button.grid(
            row=4, column=0, columnspan=2, sticky=constants.EW)

        back_button = ttk.Button(
            master=self.frame, text="Back", command=self.show_start_view)
        back_button.grid(row=5, column=0, sticky=constants.EW)

        # lisää tänne se millä saa näytölle generoidun salasanan!!

        #self.frame.grid_columnconfigure(0, weight=1, minsize=300)

    def init_frame(self):
        self.frame = ttk.Frame(master=self.root)

        self.password_gen()

        self.frame.grid_columnconfigure(0, weight=1, minsize=300)

    def generate_password(self):
        self.password_entry.delete(0, END)
        password_length = int(self.length_entry.get())
        # self.feedback.destroy()

        password = []
        all_char = string.ascii_letters + string.digits + string.punctuation

        # alkuun
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        # loput
        for i in range(1, password_length - 3):
            if len(password) < password_length:
                password.append(random.choice(all_char))

        # viimeistely
        random.shuffle(password)
        final_password = "".join(password)

        self.password_entry.insert(0, final_password)
