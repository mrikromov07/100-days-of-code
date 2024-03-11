a = input("Write 2 digit number!\n")
b = a[0]
c = a[1]
print (int(b) + int(c))

height = input ("Enter your height im m: \n")
weight = input ("Enter your weight in kg: \n")
BMI = int(weight) / ( float(height) * float(height))
print (f" Your BMI is : {int(BMI)}")