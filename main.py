from random import randint


class CreatePassword:
    item = ""
    password = ""

    def __init__(self, string):
        self.item = string

    def iterPassword(self):
        self.password = self.item[randint(0, len(self.item) - 1)]
        self.password += ''.join(self.item[randint(0, 20)] for i in range(19))
        return self.password

    def complexPassword(self):
        self.iterPassword()
        if not self.password[0].isalpha():
            return self.iterPassword()
        else:
            return self.password

    def getPwdJoin(self):
        print(self.password)

if __name__ == '__main__':
    myPwd = CreatePassword("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_")
    myPwd.complexPassword()
    myPwd.getPwdJoin()
