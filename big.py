year = int(input("year: "))
month = int(input("month: "))
date = int(input("date: "))
if year % 4 == 0:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and date <= 30:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 and date == 31:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 4 or month == 6 or month == 9 or month == 11 and date <= 29:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 4 or month == 6 or month == 9 or month == 11 and date == 30:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 2 and date <= 28:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 2 and date == 29:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 12 and date == 31:
        next_date = 1
        month1 = 1
        year1 = year + 1

    else:
        next_date = "not defined"
        month1 = "not defined"
        year1 = "not defined"
    print(f"next date of the date {year}-{month}-{date} is {year1}-{month1}-{next_date}")
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and date <= 30:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 and date == 31:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 4 or month == 6 or month == 9 or month == 11 and date <= 29:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 4 or month == 6 or month == 9 or month == 11 and date == 30:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 2 and date <= 27:
        next_date = date + 1
        month1 = month
        year1 = year
    elif month == 2 and date == 28:
        next_date = 1
        month1 = month + 1
        year1 = year
    elif month == 12 and date == 31:
        next_date = 1
        month1 = 1
        year1 = year + 1

    else:
        next_date = "not defined"
        month1 = "not defined"
        year1 = "not defined"
    print(f"next date of the date {year}-{month}-{date} is {year1}-{month1}-{next_date}")
