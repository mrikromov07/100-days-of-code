age = input("Enter your age: ")

year = 90-int(age)
month = year * 12
weeks = year * 52
days = year * 365

message = f"You have {year}years, {month}months, {weeks}weeks, {days}days left"

print(message)