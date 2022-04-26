class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged = False

        print(self.username)
        print(self.password)
        # ota noi pois käytöstä kun tietää, että ohjelma toimii
