print("\n\nWeeks of your life\n")
age = int(input("Enter your age : "))

years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left *52
days_left = years_left *365

print(f"Your remaining time is {years_left} years, \
{months_left} months, {weeks_left} weeks or {days_left} days \n\n\n")