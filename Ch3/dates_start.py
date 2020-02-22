#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(today)


  # print out the date's individual components
  print(today.month , today.day , today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Index of day : ", today.weekday())
  days = ["mon","tue","wed","thus","fri","sat","sun"]
  print("Day ", days[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("today's date with time : ", datetime.now())

  # Get the current time
  print("time : ", datetime.time(datetime.now()))


  
if __name__ == "__main__":
  main();
  