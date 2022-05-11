#from entities.save_info import Info
from entities.user import User

from repositories.user_repo import (UserRepo as default_user_repo)
#from repositories.info_repo import (InfoRepo as default_info_repo)


class InvalidCredentialsError(Exception):
    """Luokka, joka tuottaa virheen jos käyttäjänimi ja/tai salasana on virheellinen
    Args:
        Exception
    """


class UsernameExistsError(Exception):
    """Luokka, joka tuottaa virheen jos käyttäjätunnus on jo olemassa
    Args:
        Exception
    """


class Service:
    """Luokka, joka vastaa sovelluslogiikasta
    """

    def __init__(self, user_repo=default_user_repo):
        """Luokan konstruktori

        Args:
            user_repo: Olio, jollaa UserRepoa vastaavat metodit

            info_repo: olio, jolla InfoRepoa vastaavat metodit
            """

        self._user = None
        self._user_repo = user_repo
        #self.info_repo = info_repo
        # , info_repo=default_info_repo

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

        Args:
            username: Merkkijono, joka kuvaa kirjautuvaa käyttäjätunnusta

            password: Merkkijono, joka kuvaa käyttäjän salasanaa

        Returns: Palauttaa kirjautuneen käyttäjän User-oliona
        """

        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid password or username")

        self._user = user
        return user

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän

        Returns: Palauttaa kirjautuneen käyttäjän User-oliona
        """

        return self._user

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät

        Returns: Kaikki käyttäjät
        """

        return self._user_repo.find_all_users()

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):

        existis = self._user_repo.find_by_username(username)

        if existis:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repo.create_user(User(username, password))

        if login:
            self._user = user

        return user


service = Service()
