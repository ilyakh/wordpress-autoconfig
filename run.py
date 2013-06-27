from random import randint
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
            "curl", 
            "-O",
            URL
    ]

    sh < [ 
            "tar", 
            "-xvf", 
            NAME
    ]

    sh < [
            "mv",
            "./wordpress/",
            TARGET_PATH
    ]

    sh < [
            "rm",
            NAME
    ]

    sh < [
        "curl",
        "-O",
        "http://phpseclib.sourceforge.net/wordpress.zip"
    ]

    sh < [
        "unzip",
        "wordpress.zip",
        "-d",
        "./project/wp-content/plugins"
    ]


    # assign right privileges (always the final step!)
    # remember to edit file and fill in your user and group names
    sh < [
            "sh",
            "modconfig.sh"
    ]
    

