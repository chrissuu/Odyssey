from AppOpener import run, mklist


class OdysseyCmds:
    def __init__(self):
        pass

    def openApp(self, app):
        run(app)

    def printAppNames(self):
        print(str(run("ls")))
