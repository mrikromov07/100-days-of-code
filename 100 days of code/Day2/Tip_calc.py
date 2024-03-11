print("Welcome to tip calculator!")
total_bill = input ("What is your total bill?")
tip_per = input (" What percentage tip would you like to give?")
Number_person = input (" How many people to split the bill? ")
Per_added =((int(total_bill) / 100) * int(tip_per)) + int(total_bill)
Devision = int(Per_added) / int(Number_person)

print(f" Each of you should pay {round (Devision,)} $")



