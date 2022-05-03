class Info:
    def __init__(self, site, username, password, user=None):
        self.site = site
        self.username = username
        self.password = password
        self.user = user

        print(self.user)

    def set_user(self, user):
        self.user = user


# MITEN TÄNNE SAA "USER" KOHTAAN SE  HETKISEN KÄYTTÄJÄN EIKÄ "NONE"
