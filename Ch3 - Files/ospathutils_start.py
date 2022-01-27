#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
from posixpath import realpath
import time


def main():
    # Print the name of the OS
    print(os.name)

    
    # Check for item existence and type
    print("item exists:", str(path.exists("textfile.txt")))
    print("item is a file:", path.isfile("textfile.txt"))
    print("item is a directory:", path.isdir("textfile.txt"))

    
    # Work with file paths
    print("item's path is:", path.realpath("textfile.txt"))
    print("item's path and name is:", path.split(path.realpath("textfile.txt")))

    
    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

    print("it has been", td, "since file was modified")
    print("or, ", td.total_seconds(), "seconds")

  
if __name__ == "__main__":
    main()
