from repositories.user_repo import (UserRepo as default_user_repo)


class InvalidCredentialsError(Exception):
    """Luokka, joka tuottaa virheen jos käyttäjänimi ja/tai salasana on virheellinen

        Args:
            Exception
    """


class Service:
    """Luokka, joka vastaa sovelluslogiikasta"""

    def __init__(self, user_repo=default_user_repo):
        """Luokan konstruktori

        Args:
            user_repo: Olio, jollaa UserRepoa vastaavat metodit

            info_repo: olio, jolla InfoRepoa vastaavat metodit
        """

        self.user = None
        self.user_repo = user_repo

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

            Args:
                username: Merkkijono, joka kuvaa kirjautuvaa käyttäjätunnusta

                password: Merkkijono, joka kuvaa käyttäjän salasanaa

            Returns: Palauttaa kirjautuneen käyttäjän User-oliona
        """

        user = self.user_repo.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid password or username")

        self.user = user
        return user

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän

            Returns: Palauttaa kirjautuneen käyttäjän User-oliona
        """

        return self.user

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät

            Returns: Kaikki käyttäjät
        """

        return self.user_repo.find_all_users()

    def logout(self):
        self.user = None


service = Service()
