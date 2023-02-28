from CreatePassord import *

@app.command()
def newPassword(number: int = typer.Option(20, help="le nombre de signe par défaut est de 20")):
    if number:
        typer.confirm(f"The password will be {number} signs, [it's OK]", abort=True)
        myPwd = CreatePassword(number)
        myPwd.complexPassword()
        myPwd.getPwdJoin()


if __name__ == '__main__':
    app()
