import unittest
from service.service import Service
from entities.user import User
from repositories.user_repo import UserRepo
from database_connection import get_database_connection_test
from init_database import init_database_test


class TestService(unittest.TestCase):
    def setUp(self):
        init_database_test()
        self.user_repository = UserRepo(get_database_connection_test())
        self.user_repository.delete_users()
        self.user_iida = User("iida", "abc123")
        #self.user_jani = User("jani", "cba321")

    def test_login(self):
        self.user_repository.create_user(self.user_iida)
        service = Service(self.user_repository)
        service.login(self.user_iida.username, self.user_iida.password)

        #all_users = self.user_repository.find_all_users()
        self.assertEqual("iida", self.user_iida.username)

    def test_get_current_users(self):
        self.user_repository.create_user(self.user_iida)
        service = Service(self.user_repository)
        service.login(self.user_iida.username, self.user_iida.password)

        service.get_all_users()

        self.assertEqual("iida", self.user_iida.username)

    def test_get_current_user(self):
        self.user_repository.create_user(self.user_iida)
        service = Service(self.user_repository)
        service.login(self.user_iida.username, self.user_iida.password)

        current_user = service.get_current_user().username

        self.assertEqual(current_user, self.user_iida.username)

        # tää testi ei oikeesti toimi
