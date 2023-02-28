import unittest
from main import CreatePassword


class TestCreatePassword(unittest.TestCase):

    def test_sort_password(self):
        myPwd = CreatePassword("abcdefghijklmnopqrstuvwxyz")
        password = myPwd.iterPassword()
        self.assertEqual(len(password), 20)

    def test_final_password_starts_with_letter(self):
        myPwd = CreatePassword("abcdefghijklmnopqrstuvwxyz")
        myPwd.iterPassword()
        password = myPwd.complexPassword()
        self.assertTrue(password[0].isalpha())

    def test_final_password_no_digits(self):
        myPwd = CreatePassword("abcdefghijklmnopqrstuvwxyz")
        myPwd.iterPassword()
        password = myPwd.complexPassword()
        self.assertTrue(all(c.isalpha() for c in password))


if __name__ == '__main__':
    unittest.main()
