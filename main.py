import re
from random import randint


def createPassword():
    index = 0
    regex = "(A&1B2C3D4E5F_+6G7H8I9@J8b7c6d5e4f2g1hijklmnopqr1234#56stuvwxyzKLMNOPQRSTUVWXYZ)"
    password = ""
    for i in regex:
        if index < 20:
            password += regex[randint(0, 60)]
            index += 1

    return password


if __name__ == '__main__':
   createPassword()