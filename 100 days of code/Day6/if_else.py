"""1-mashq"""

# cars = ['Nexia', 'Cobalt', 'bmw', 'Gentra']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

"""2-mashq"""

# cars = ['Nexia', 'Cobalt', 'bmw', 'Gentra']

# for car in cars:
#     if car != 'bmw':
#         print(car.title())
#     else:
#         print(car.upper())


"""3-mashq"""

""" Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. 
Foydalanuvchilar ro'yxatini ko'rasizmi?" 
xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  
matnini konsolga chiqaring. """

# admin = 'Ali'
# login = input("Ismingiz nima?")
# if login.lower() == admin.lower():
#     print("Xush kelibsiz admin! Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")


"""4-mashq"""

# sonlar=[]

# for n in range(2):
#     sonlar.append(input(f"{n+1} chi sonni kiriting: "))
    
# if sonlar[0]== sonlar[1]:
#         print(f"{sonlar[0]} va {sonlar[1]} teng!")
# else:
#         print(f"{sonlar[0]} va {sonlar[1]} teng emas!")



"""5-mashq"""

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat")

"""6-mashq"""

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')