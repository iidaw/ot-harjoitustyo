from tkinter import Tk, ttk, constants, END


class PasswordGeneratorView:
    def __init__(self):
        self.root = Tk()
        self.root.title("Password Generator")

        self.length_label = ttk.Label(self.root, text="Enter length (number):")
        self.length_label.grid(row=0, column=0, columnspan=2)

        self.length_entry = ttk.Entry(self.root)
        self.length_entry.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W))

        self.password_label = ttk.Label(self.root, text="Generated Password:")
        self.password_label.grid(row=2, column=0, columnspan=2)

        self.password_entry = ttk.Entry(self.root, text="")
        self.password_entry.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

        generate_button = ttk.Button(self.root, text="Generate", command=self.generate_password)
        generate_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W))

        self.root.grid_columnconfigure(1, weight=1, minsize=300)

        self.password_length = int
        self.final_password = ""