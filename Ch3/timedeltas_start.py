#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=4, minutes=34))


# print today's date
now = datetime.now()
print("today : " + str(now), now.date())


# print today's date one year from now
print("today's date one year from now : " + str(now+ timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days anf 3 weeks it will be : " + str(now+ timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
print("the date 1 week ago : " + str(now - timedelta(weeks=1)))


### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4,1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fool's day already went by %d days ago " %((today-afd).days))
    afd = afd.replace(year = today.year + 1)
else:
    print("April fool day is yet to come")


# Now calculate the amount of time until April Fool's Day  
print("Next april fool day will be in %d days" %((afd-today).days))


