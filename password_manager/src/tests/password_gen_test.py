import unittest
from password_generation import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        password = PasswordGenerator()
        pw = password.generate_password(8)
        

        self.assertEqual(len(pw), 8)

        