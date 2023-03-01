import re
import unittest
from CreatePassord import CreatePassword

regex = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_"


class TestCreatePassword(unittest.TestCase):

    def test_sort_password(self):
        myPwd = CreatePassword(20, regex)
        password = myPwd.iterPassword()
        self.assertEqual(len(password), 20)

    def test_final_password_starts_with_letter(self):
        myPwd = CreatePassword(20, regex)
        myPwd.iterPassword()
        password = myPwd.complexPassword()
        self.assertTrue(password[0].isalpha())

    def test_final_password_no_digits(self):
        myPwd = CreatePassword(20, regex)
        myPwd.iterPassword()
        password = myPwd.complexPassword()
        self.assertTrue(re.search(r"\w", password[0]))


if __name__ == '__main__':
    unittest.main()
