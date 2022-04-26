
#from entities.save_info import Info
from entities.user import User

from repositories.user_repo import UserRepo
from repositories.info_repo import InfoRepo


# class PasswordService:
#   def __init__(self):
#      self._user = None

# def add_info(self, site, username, password):
#    info = Info(user=self._user, site=site, username=username, password=password)

#   return info


class Service:
    def __init__(self, user_repo: UserRepo, info_repo: InfoRepo):
        self._user = None
        self._user_repo = user_repo
        self.info_repo = info_repo

    # def add_information(self):
      #  information = Info(site, username, password)

    def login(self, username, password):
        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            return "Invalid username or password"

        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_all_users(self):
        return self._user_repo.find_all_users()

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        existis = self._user_repo.find_by_username(username)

        if existis:
            return "Username existis"

        user = self._user_repo.create_user(User(username, password))

        if login:
            self._user = user

        return user


#password_service = PasswordService()
#user_service = UserService()


# kesken
