"""1-mashq"""

ismlar = ['Boburjon', 'Xurshidbek', 'Muhammad Nosir', 'Javohir','Muhammadyusuf','Sohibjon']

for ism in ismlar:
    print(f"Salom {ism}, Ertaga fudbolga boramizmi?")
print("Kod 6 marta takrorlandi!")

"""2-mashq"""
toq_sonlar = list(range(10,100))

for kub in toq_sonlar:
    print(f"{kub}ning kubi: {kub**3}")
    
"""3-mashq"""

kinolar = []
print('5ta eng yoqtirgan kinolaringizni kiriting!')

for kino in range(5):
    kinolar.append(input(f"{kino + 1} chi kinoni kiriting: "))
print(kinolar)

"""4-mashq"""

odamlar = []

print("Bugun nechta odamlar bilan ko'rishdingiz? ")

for odam in range(int(input())):
    odamlar.append(input(f"{odam+1}chi odam ismini kiriting: "))
print(odamlar)