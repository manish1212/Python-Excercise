#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  # print(os.name)


  # Check for item existence and type
  # print("Item exists : " + str(path.exists("textfile.txt")))
  # print("Item is a file : " + str(path.isfile("textfile.txt")))
  # print("Item is a directory : " + str(path.isdir("textfile.txt")))

  
  # Work with file paths
  print("Item's path : " + str(path.realpath("textfile.txt")))
  print("Item's path and name : " + str(path.split(path.realpath("textfile.txt"))))

  
  # Get the modification time

  
  # Calculate how long ago the item was modified


  
if __name__ == "__main__":
  main()
