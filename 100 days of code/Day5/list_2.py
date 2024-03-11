countries = ['Uzbekistan','USA', 'Canada', "Russia", 'Poland']
countries.reverse()
a = list(range(120, 1201, 2))

# 2 - mashq

taomlar = ['Osh', "Sho'rva", 'Mastava', 'Lagman', 'Bishteks']
nonushta = taomlar
taomlar.insert(0,'Manti')
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
print(taomlar)

print(f"Ro'yxat uzunligi: {len(countries)}")
print(f"Ro'yxat uzunligi: {sorted(countries)}")
print(f"Ro'yxat uzunligi: {sorted(countries, reverse=True)}")
print(f"Asl ro'yxat: {countries}")
print(f"Ro'yxat ortidan: {countries}")
print(f"Alifbo bo'yicha: {sorted(countries)}")
print(f"Teskaari Alifbo bo'yicha: {sorted(countries, reverse = True)}")
print(f"Juft sonlar: {a}")
print(f"Eng kichik son: {min(a)}")
print(f"Eng katta son: {max(a)}")
print(f"Eng katta sondan eng kichik son ayirmasi: {max(a) - min(a)}")
print(f"Sonlar yig'indisi: {sum(a)}")
print(f"Sonlar boshidan 20ta: {a[:21]}")


