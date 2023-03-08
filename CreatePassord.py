from random import randint


regex = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_"


class CreatePassword:
    item = ""
    password = ""
    nbr = 0

    def __init__(self, nbr: int = 20, string: str = regex):
        self.item = string
        self.nbr = nbr
   
    def iterPassword(self):
        self.password = self.item[randint(0, len(self.item))]
        self.password += ''.join(self.item[randint(0, self.nbr)] for i in range(self.nbr - 1))
        return self.password

    def complexPassword(self):
        self.iterPassword()
        if not self.password[0].isalpha():
            print(self.iterPassword())
            return self.iterPassword()
        else:
            print(self.password)
            return self.password

    def getPwdJoin(self):
        print(f"Here the password \"{self.password}\" that comport {len(self.password)} signs")
