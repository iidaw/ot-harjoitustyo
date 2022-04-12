#import uuid


class Info:
    def __init__(self, site, username, password, user=None):
        self.site = site
        self.username = username
        self.password = password
        self.user = user
