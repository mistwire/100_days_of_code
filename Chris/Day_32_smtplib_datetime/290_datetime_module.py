import datetime as dt


# get current date & time
now = dt.datetime.now()
print(now)

# with that you can tap into the individual attribs:
year = now.year
print(year)
month = now.month
print(month)
day_of_week = now.weekday()
print(day_of_week)

# create a datetime object from scratch:
date_of_birth = dt.datetime(year=1973, month=4, day=9)
print(date_of_birth)

