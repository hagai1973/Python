year_checked = int(input("Type year you want to check if it leap or not: "))

leap = False

if year_checked%4==0:
 if year_checked%100!=0:
  leap=True
 elif year_checked%400==0:
  leap=True

if leap:
 print(f"The year {year_checked} is a leap")
else:
 print(f"The year {year_checked} is NOT a leap")