your_age = input("what is your current age:")

time_left = 90 - int(your_age)

days = 365 * time_left
weeks = 52 * time_left
months = 12 * time_left


print(f"You have {days} days, {weeks} weeks, and {months} left :) ")