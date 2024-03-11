Year = int(input("What year do you want to check?"))

if Year % 4 == 0:
    print("Leap year!")
elif Year % 100 == 0:
    if Year % 400 == 0:
        print("Leap year!")
    else:
        print("Not Leap year!")
else:
    print("Not Leap year!")