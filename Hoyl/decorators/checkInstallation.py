coeficient = -2 if __name__=="__main__" else -1

import sys
sys.path.append(f"{ "\\".join(sys.path[0].split('\\')[:coeficient]) }")

import os
from submodules import jsonManager

def checkInstallation(func):
    def wrapper(*args, **kwargs):
        
        assert os.path.exists("hoyl.json"), "\"Hoyl.json\" file does not exist. Please run \"hoyl init\" to create it."

        checker = jsonManager.checker("hoyl.json", {
            "hasTemplate": bool,
            "componentsPath": str,
            "routerPath": str,
            "routerControlFile": str,
            "pagesPath": str,
            "templateFile": str,
            "tsEnable": bool
        })

        endingWords = {
            "missing": "is missing the following keys",
            "extra": "has the following extra keys",
            "wrongType": "has the following keys with wrong types"
        }

        for item in checker.keys():
            assert len(checker[item]) == 0, f"\"hoyl.json\" file { endingWords[item] }: { checker[item] }, please run \"hoyl init\" to fix it."

        return func(*args, **kwargs)
    return wrapper