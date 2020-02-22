#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  
  print(now.strftime("%Y %d %b %a"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print("locale's date and time", now.strftime("%c"))
  print("locale's date", now.strftime("%x"))
  print("locale's time", now.strftime("%X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime(" Time Formatting : %I %M %S %p"))



if __name__ == "__main__":
  main();
