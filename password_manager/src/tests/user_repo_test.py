import unittest
from repositories.user_repo import UserRepo
from entities.user import User
from database_connection import get_database_connection_test
from init_database import init_database_test


class TestUserRepo(unittest.TestCase):
    def setUp(self):
        init_database_test()
        self.user_repository = UserRepo(get_database_connection_test())
        self.user_repository.delete_users()
        self.user_iida = User("iida", "abc123")
        self.user_anna = User("anna", "def456")

    def test_create(self):
        self.user_repository.create_user(self.user_iida)
        all_users = self.user_repository.find_all_users()
        self.assertEqual(all_users[0].username, self.user_iida.username)

    def test_find_all_users(self):
        self.user_repository.create_user(self.user_iida)
        self.user_repository.create_user(self.user_anna)
        all_users = self.user_repository.find_all_users()
        self.assertEqual(all_users[0].username, self.user_iida.username)
        self.assertEqual(all_users[1].username, self.user_anna.username)

    def test_find_by_username(self):
        self.user_repository.create_user(self.user_iida)
        user = self.user_repository.find_by_username(self.user_iida.username)
        self.assertEqual(user.username, self.user_iida.username)
