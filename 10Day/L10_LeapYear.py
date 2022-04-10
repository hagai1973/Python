# year_checked = int(input("Type year you want to check if it leap or not: "))


def check_leap(year_checked):
    if year_checked%4==0:
        if year_checked%100!=0:
            return True
        elif year_checked%400==0:
            return True
    return False
