""" 1-mashq"""

son = float(input("Juft son kiriting: "))
if son%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")
    
""" 2-mashq"""

user = int(input("Yoshingizni kiriting: "))

if user <= 4 or user >= 60 :
    print (" Kirish bepul!")
elif user <= 18 :
    print(" Kirish 10 000 so'm ")
elif user >= 18 :
    print("Kirish 20 000 so'm")

""" 3-mashq"""

sonlar = []

for son in range(2):
    sonlar.append(input((f"{son+1}chi sonni kiriting: ")))
if sonlar[0] > sonlar[1]:
    print(f"{sonlar[0]} > {sonlar[1]} ")
else:
    print(f"{sonlar[0]} < {sonlar[1]} ")

""" 4-mashq"""

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
    



""" 5-mashq"""

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
yoq_mahsulotlar = []

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        yoq_mahsulotlar.append(mahsulot)
if yoq_mahsulotlar:
    print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in yoq_mahsulotlar:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")



""" 6-mashq """

users = ['Anvar', 'Bobur', 'Tohir', 'Xurshid', 'Javohir']

login = input("Yangi login kiriting: \n")

if login in users:
    print(f"{login.title()} logini band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}!")


""" 7-mashq """

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    else:
        print(f" Bu son faqat qoldiqli bo'linadi!")
