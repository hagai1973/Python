from datetime import date
import L10_LeapYear

def days_in_month(month_number = 2, year = 2000):
    """Return the number of day in month
    Args:
        month_number (int):the month number want to check
        year (int): the month's year (verify that the year is leap or not)

    Returns:
        int: numbers of days in rquired month
    """
    
    if month_number > 12 or month_number < 1:
        return f"incorrect vlaue: {month_number}"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (month_number != 2):
        return month_days[month_number -1]
    else:
        # if (L10_LeapYear.check_leap(date.today().year)):
        if (L10_LeapYear.check_leap(year)):
            return month_days[month_number -1] + 1
        else:
            return month_days[month_number -1]
        


print (days_in_month(2, 2000))