#!/usr/bin/env python3

# ##################################################################
#
#
#
# projecteuler.net problem 19
#
#
# How Sundays fell on the first of the month in the twentieth century?
#
#
#
#
#
#
#
# #####################################################################3


from datetime import date, timedelta


START_DATE = date(1901, 1, 1)
END_DATE = date(2000, 12, 31)


def is_sunday(date):
    """
    Returns true if the day is a Sunday.
    Maybe be subject to errors if date is too far away from START_DATE.

    TODO: Allow different start dates (use START_DATE.weekday())
    """
    WEEK = timedelta(weeks=1)
    FIVE = timedelta(days=5)
    delta = date - START_DATE

    return True if delta % WEEK == FIVE else False


def months_to_check():
    """
    yields a date object for each month in the given years

    returns the first day of the month.

    TODO: Return a different day if specified
    TODO: Return partial years at start and end
    """
    for year in range(START_DATE.year, END_DATE.year + 1):
        for month in range(1, 12 + 1):
            yield date(year, month, 1)

    raise StopIteration


def check_months():
    count = 0
    for month in months_to_check():
        if is_sunday(month):
            count += 1

    return count


if __name__ == '__main__':
    print(check_months())
