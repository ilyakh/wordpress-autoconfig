from core import *

VERSION = "3.5.2"
PREFIX = "wordpress-"
SUFFIX = "-nb_NO.tar.gz"

REPOSITORY = "http://nb.wordpress.org/" 
NAME = PREFIX + VERSION + SUFFIX
URL = REPOSITORY + NAME

TARGET_PATH = "project"

if __name__ == "__main__":

    sh = shell()

    sh < [
            "rm", 
            "-rf",
            "wordpress"
    ]
    
    sh < [
            "rm",
            "-rf",
            "project"
    ]

    
