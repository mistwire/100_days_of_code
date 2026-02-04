# KEY CONCEPT: Return values enable functions to compute and send data back to caller
# These functions RETURN information instead of just printing

def is_leap(year):
    """Check if a year is a leap year according to Gregorian calendar rules."""
    # ALGORITHM: Leap year rules (order matters!)
    # 1. Divisible by 400 → leap year
    # 2. Divisible by 100 (but not 400) → not leap year
    # 3. Divisible by 4 (but not 100) → leap year
    # 4. Otherwise → not leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # e.g., 2000 is leap
            else:
                return False  # e.g., 1900 is not leap
        else:
            return True  # e.g., 2004 is leap
    else:
        return False  # e.g., 2003 is not leap

def days_in_month(year, month):
    """Return the number of days in a given month (accounting for leap years)."""
    # Standard days per month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # SPECIAL CASE: February in a leap year has 29 days instead of 28
    # KEY CONCEPT: Calling one function from another function
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]  # month is 1-indexed, list is 0-indexed

#🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)

