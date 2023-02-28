from random import randint


class CreatePassword:
    item = ""
    password = ""
    nbr = 0

    def __init__(self, string, nbr):
        self.item = string
        self.nbr = nbr

    def iterPassword(self):
        self.password = self.item[randint(0, len(self.item))]
        self.password += ''.join(self.item[randint(0, self.nbr)] for i in range(self.nbr - 1))
        return self.password

    def complexPassword(self):
        self.iterPassword()
        if not self.password[0].isalpha():
            return self.iterPassword()
        else:
            return self.password

    def getPwdJoin(self):
        print(self.password, len(self.password))

if __name__ == '__main__':
    myPwd = CreatePassword("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_", 30)
    myPwd.complexPassword()
    myPwd.getPwdJoin()
