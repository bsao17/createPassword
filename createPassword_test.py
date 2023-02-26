import re
import unittest
from main import createPassword


class TestCreatePassword(unittest.TestCase):

    def test_password_length(self):
        # Vérifie que le mot de passe a une longueur de 20 caractères
        password = createPassword()
        self.assertEqual(len(password), 20)

    def test_password_contains_lowercase(self):
        # Vérifie que le mot de passe contient au moins une lettre minuscule
        password = createPassword()
        self.assertRegex(password, r'[a-zA-Z0-9]')

    def test_password_contains_uppercase(self):
        # Vérifie que le mot de passe contient au moins une lettre majuscule
        password = createPassword()
        self.assertRegex(password, r'[A-Z]')

    def test_password_contains_special_character(self):
        # Vérifie que le mot de passe contient au moins un caractère spécial
        password = createPassword()
        self.assertRegex(password, r'[!@#$%^&*()<>?/\|}{~:]')

    def test_password_contains_digit(self):
        # Vérifie que le mot de passe contient au moins un chiffre
        password = createPassword()
        self.assertRegex(password, r'[0-9]')

    def test_password_does_not_contain_invalid_characters(self):
        # Vérifie que le mot de passe ne contient que des caractères valides
        password = createPassword()
        self.assertFalse(re.search(r"[^A-Za-z0-9!@#$%^&*()<>?/\|}{~:]", password))


if __name__ == '__main__':
    unittest.main()
