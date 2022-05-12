from tkinter import END, messagebox, ttk, constants
from repositories.info_repo import InfoRepo
from service.service import Service
from entities.save_password_info import PasswordInfo


class AddPasswordView:
    """Luokka vastaa salasananäkymästä ja sen näkymisestä
    """

    def __init__(self, root, service: Service, info_repo: InfoRepo, show_start_view, show_password_gen_view):
        """Luokan konstruktori

            Args:
                root: tkinter-elementti, jonka avulla näkymä alustetaan

                service: viittaa luokkaan Service, joka vastaa sovelluslogiikasta

                info_repo: viittaa luokkaan InfoRepo, joka vastaa tallennetuista salasanatiedoista

                show_start_view: tämän avulla päästään uloskirjautuessa takaisin alkunäkymään
        """

        self.root = root
        self.frame = None
        self.service = service
        self.info_repo = info_repo
        self.site_entry = None
        self.username_entry = None
        self.password_entry = None
        self.show_start_view = show_start_view
        self.show_password_gen_view = show_password_gen_view

        self.initialize()

    def pack(self):
        """Näyttää näkymän"""

        self.frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""

        self.frame.destroy()

    def add_info_handle(self):
        """Mahdollistaa salasanan tallentamisen tietokantaan, itse toiminnosta vastaa InfoRepo luokka
        """

        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(site) >= 1 and len(username) >= 1 and len(password) >= 1:
            self.info_repo.add_password_info(
                PasswordInfo(site, username, password, self.service.get_current_user().username))
            self.add_info_messagebox()

        else:
            self.error_messagebox()

        self.treeview()

    def error_messagebox(self):
        messagebox.showinfo("empty", "Site, Username and Password required")

    def add_info_messagebox(self):
        messagebox.showinfo("", "Password information added")

    def treeview(self):
        """Vastaa salasanojen näkymisestä"""

        tree = ttk.Treeview(self.frame, column=(
            "site", "username", "password"), show="headings", selectmode="browse")

        tree.heading("site", text="Site/ App")
        tree.heading("username", text="Username")
        tree.heading("password", text="Password")

        tree.grid(row=9, column=0, columnspan=2, sticky=constants.EW)

        passwords = self.info_repo.find_passwords_by_user(
            self.service.get_current_user().username)

        for password in passwords:
            tree.insert("", END, values=(password.site,
                        password.username, password.password))

    def initialize(self):
        """Vastaa näkymän asettelusta"""

        self.frame = ttk.Frame(master=self.root)

        current_user_label = ttk.Label(
            master=self.frame, text=f"Logged in as {self.service.get_current_user().username}", font="Arial 15")
        current_user_label.grid(
            row=0, column=0, columnspan=2, sticky=constants.W)

        label = ttk.Label(master=self.frame,
                          text="Add information", font="Arial 20")
        label.grid(row=2, column=0, columnspan=2, sticky=constants.W)

        site_label = ttk.Label(
            master=self.frame, text="Site/ App: ", font="Arial")
        site_label.grid(row=3, column=0, sticky=constants.W)

        self.site_entry = ttk.Entry(master=self.frame)
        self.site_entry.grid(row=4, column=0, sticky=constants.EW)

        username_label = ttk.Label(
            master=self.frame, text="Username:", font="Arial")
        username_label.grid(row=5, column=0, sticky=constants.W)

        self.username_entry = ttk.Entry(master=self.frame)
        self.username_entry.grid(row=6, column=0, sticky=constants.EW)

        password_label = ttk.Label(
            master=self.frame, text="Password:", font="Arial")
        password_label.grid(row=7, column=0, sticky=constants.W)

        self.password_entry = ttk.Entry(master=self.frame)
        self.password_entry.grid(row=8, column=0, sticky=constants.EW)

        self.treeview()

        password_generator_button = ttk.Button(
            master=self.frame, text="Generate Password", command=self.show_password_gen_view)
        password_generator_button.grid(
            row=10, column=0, columnspan=2, sticky=constants.EW)

        add_button = ttk.Button(
            master=self.frame, text="Add infromation", command=self.add_info_handle)

        add_button.grid(row=11, column=0, columnspan=3, sticky=constants.EW)

        logout_button = ttk.Button(
            master=self.frame, text="Log out", command=self.show_start_view)
        logout_button.grid(row=12, column=0, columnspan=2, sticky=constants.EW)

        empty_label = ttk.Label(master=self.frame)
        empty_label.grid(row=13, column=0)

        self.frame.grid_columnconfigure(0, weight=1, minsize=500)
