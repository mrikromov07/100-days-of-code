print("Welcome to Pizza delivery!")
size = input("What size pizza do you want? S,M or L")
add_sariq = input (" Do you want Sariq? Y or N")
extra = input ("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 30
    
if add_sariq == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra == "Yes":
    bill +=1

print(f"Your final bill is ${bill}")
    
    


   
    