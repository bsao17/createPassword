from numbers import Number
import re
from random import randint


class CreatePassword:
    regex = ""
    password = ""
    password_join = ""

    def __init__(self, string):
        self.regex = string

    def sortPassword(self):
        self.password = self.regex[randint(0, 20)]
        self.password += ''.join(self.regex[randint(0, 20)] for i in range(19))
        return self.password

    def finalPassword(self):
        if not self.password[0].isalpha():
            return self.sortPassword()
        else:
            return self.password


    def getPwdJoin(self):
        print(self.password)


if __name__ == '__main__':
    myPwd = CreatePassword("123456789abcdefghijklmnopqrstuvwxyz")
    myPwd.sortPassword()
    myPwd.finalPassword()
    myPwd.getPwdJoin()
