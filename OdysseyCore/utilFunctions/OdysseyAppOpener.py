from AppOpener import run, mklist


class OdysseyAppOpener:
    def __init__(self):
        pass

    def __str__(self):
        return "openApp|printAppNames"

    def openApp(self, app):
        run(app)

    def printAppNames(self):
        print(str(run("ls")))

