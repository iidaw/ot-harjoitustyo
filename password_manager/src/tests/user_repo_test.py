import unittest
from repositories.user_repo import UserRepo
from entities.user import User
from database_connection import get_database_connection_test
from init_database import init_database_test
from repositories.info_repo import InfoRepo
from entities.save_password_info import PasswordInfo


class TestUserRepo(unittest.TestCase):
    def setUp(self):
        init_database_test()
        self.user_repository = UserRepo(get_database_connection_test())
        self.user_iida = User("iida", "abc123")
        self.user_anna = User("anna", "def456")

    def test_create_user(self):
        self.user_repository.create_user(self.user_iida)
        all_users = self.user_repository.find_all_users()
        self.assertEqual(all_users[0].username, self.user_iida.username)


class TestInfoRepo(unittest.TestCase):
    def setUp(self):
        init_database_test()
        self.info_repo = InfoRepo(get_database_connection_test())
        self.password_iida1 = PasswordInfo("moodle", "iidab", "abc123", "iida")
        self.password_iida2 = PasswordInfo("labtool", "iidab", "abc", "iida")
        self.password_anna = PasswordInfo("labtool", "annae", "def123", "anna")

    def test_add_password_info(self):
        self.info_repo.add_password_info(self.password_iida1)
        self.info_repo.add_password_info(self.password_iida2)
        self.info_repo.add_password_info(self.password_anna)
        passwords = self.info_repo.find_passwords_by_user("iida")
        self.assertEqual(len(passwords), 2)
