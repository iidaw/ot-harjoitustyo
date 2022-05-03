from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.password_gen_view import PasswordGeneratorView
from ui.start_screen import StartScreen
from ui.add_passwords_view import AddPasswordView


class UI:
    """Luokka vastaa käyttöliittymän toiminnasta ja siitä, miten näkymät vaihtuvat
    """

    def __init__(self, root, user_repo, service, info_repo):
        self.root = root
        self.current_view = None
        self.user_repo = user_repo
        self.service = service
        self.info_repo = info_repo

    def start(self):
        self.show_start_view()

    def handle_login(self):
        self.show_login_view()

    def handle_create_user(self):
        self.show_create_user_view()

    def handle_pass_gen(self):
        self.show_password_gen_view()

    def handle_password(self):
        self.show_add_password_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_start_view(self):
        self.hide_current_view()

        self.current_view = StartScreen(
            self.root, self.show_login_view, self.show_create_user_view, self.show_password_gen_view)

        self.current_view.pack()

    def show_password_gen_view(self):
        self.hide_current_view()

        self.current_view = PasswordGeneratorView(
            self.root, self.show_start_view)

        self.current_view.pack()

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root, self.handle_create_user, self.handle_password, self.show_start_view, self.service)

        self.current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateUserView(
            self.root, self.handle_login, self.handle_create_user, self.show_start_view, self.user_repo)

        self.current_view.pack()

    def show_add_password_view(self):
        self.hide_current_view()

        self.current_view = AddPasswordView(
            self.root, self.service, self.info_repo, self.show_start_view)

        self.current_view.pack()

    # jotenki pitää näyttä tallennetut salasanat
