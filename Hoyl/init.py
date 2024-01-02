# Essential Imports
import os

# System Imports
from decorators import checkInstallation

def init():
    assert os.path.exists("vite.config.js"), "\"vite.config.js\" file does not exist. Create a project with Vite and try again."

    desiredKeys = [
        "hasTemplate",
        "componentsPath",
        "routerPath",
        "routerControlFile",
        "pagesPath",
        "templateFile",
        "tsEnable"
    ]

    if not os.path.exists("hoyl.json"):

        # TODO: Vai criar todo o arquivo

        return

    # TODO: Vai entrar no modo de manutenção

    check = checkInstallation()


    # hoylJson = {

    # }

    # if check["extra"]

    # assert check["missing"]

if __name__=="__main__":
    init()