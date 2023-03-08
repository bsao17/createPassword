from random import randint


regex = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_"


class CreatePassword:
    item = ""
    password = ""

    def __init__(self, item: str = regex):
        self.item = item
   
    def iterPassword(self):
        self.password = self.item[randint(0, len(self.item) - 1)]
        self.password = ''.join(self.item[randint(0, len(self.item) - 2)] for i in range(len(self.item)))
        return self.password

    def complexPassword(self):
        self.iterPassword()
        if not self.password[0].isalpha():
            print(self.iterPassword())
            return self.iterPassword()
        else:
            print(self.password)
            return self.password
