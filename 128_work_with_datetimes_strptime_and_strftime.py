# In this Bite you get some more practice with datetime's useful strptime and stftime.

# Complete the two functions: years_ago and convert_eu_to_us_date following the instructions in their docstrings.

# This is the definition and difference between the two:

# strptime: parse (convert) string to datetime object.
# strftime: create formatted string for given time/date/datetime object according to specified format.
# Reference: 8.1.8. strftime() and strptime() Behavior. Good luck and keep calm and code in Python!

from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
    Convert this date str to a datetime object (use strptime).
    Then extract the year from the obtained datetime object and subtract
    it from the THIS_YEAR constant above, returning the int difference.
    So in this example you would get: 2018 - 2015 = 3"""
    date_year = datetime.strptime(date, "%d %b, %Y").year
    return THIS_YEAR - date_year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
    Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
    To enforce the use of datetime's strptime / strftime (over slicing)
    the tests check if a ValueError is raised for invalid day/month/year
    ranges (no need to code this, datetime does this out of the box)"""
    datetime_object = datetime.strptime(date, "%d/%m/%Y")
    return datetime_object.strftime("%m/%d/%Y")
