import unittest
from repositories.user_repo import UserRepo
from entities.user import User
from database_connection import get_database_connection_test
from init_database import init_database_test
from service.service import Service
from service.password_generator import password_generator


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


class TestService(unittest.TestCase):
    def setUp(self):
        init_database_test()
        self.user_repository = UserRepo(get_database_connection_test())
        self.user_repository.delete_users()
        self.user_iida = User("iida", "abc123")

    def test_login(self):
        self.user_repository.create_user(self.user_iida)
        service = Service(self.user_repository)
        service.login(self.user_iida.username, self.user_iida.password)

        self.assertEqual("iida", self.user_iida.username)

    def test_get_current_user(self):
        self.user_repository.create_user(self.user_iida)
        service = Service(self.user_repository)
        service.login(self.user_iida.username, self.user_iida.password)

        current_user = service.get_current_user().username

        self.assertEqual(current_user, self.user_iida.username)


class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        pass

    def test_pass_gen(self):
        generated_password = password_generator(10)

        self.assertEqual(len(generated_password), 10)
