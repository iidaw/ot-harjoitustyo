class User:
    """Luokka kuvaa yksittäistä käyttäjää"""

    def __init__(self, username, password):
        """Luokan konstruktori

            Args:
                username: merkkijono, käyttäjän tunnus
                password: merkkijono, käyttäjän salasana
                """

        self.username = username
        self.password = password
        #self.logged = False

    def user_id(self, username):
        self.username = username
