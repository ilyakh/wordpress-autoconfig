from subprocess import call
from random import randint


VERSION = "3.5.2"
PREFIX = "wordpress-"
SUFFIX = "-nb_NO.tar.gz"

REPOSITORY = "http://nb.wordpress.org/" 
NAME = PREFIX + VERSION + SUFFIX
URL = REPOSITORY + NAME

TARGET_PATH = "project"

if __name__ == "__main__":

    call([
            "rm", 
            "-rf",
            "wordpress"
    ])
    
    call([
            "rm",
            "-rf",
            "project"
    ])

    
