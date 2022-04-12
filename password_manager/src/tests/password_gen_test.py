import unittest
from password_generation_testaus import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        password = PasswordGenerator()
        pword = password.generate_password(8)

        self.assertEqual(len(pword), 8)
