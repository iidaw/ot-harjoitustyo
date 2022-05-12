class PasswordInfo:
    """Luokka kuvaa yksittäistä käyttäjä/ salasanatietoa"""

    def __init__(self, site, username, password, user):
        """Luokan konstruktori

            Args:
                site: merkkijono, kuvaa tallennetun sivuston/ ohjelman nimeä

                username: merkkijono, kuvaa sivustolle käytettyä käyttäjätunnusta

                password: merkkijono, kuvaa sivustolle käytettyä salasanaa

                user: merkkijono, kuvaa käyttäjää, jonka tallentama tieto on
        """

        self.site = site
        self.username = username
        self.password = password
        self.user = user
