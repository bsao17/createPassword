from random import randint
import typer

app = typer.Typer()

regex = " 123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$_"


class CreatePassword:
    item = ""
    password = ""
    nbr = 0

    def __init__(self, nbr: int, string: str = regex):
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
        print(f"Here the password \" {self.password} \" that comport {len(self.password)} signs")


@app.command()
def newPassword(number: int = typer.Option(20, help="le nombre de signe par défaut est de 20")):
    if number:
        typer.confirm(f"The password will be {number} signs, [it's OK]", abort=True)
        myPwd = CreatePassword(number)
        myPwd.complexPassword()
        myPwd.getPwdJoin()


if __name__ == '__main__':
    app()
