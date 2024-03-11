# cars = []
# cars.append('Cobalt')
# cars.append('Nexia')
# cars.append('Malibu')
# cars.append('Spark')

# print(cars)

# friends = ['Boburjon','Xurshidbek','Muhammad Nosir']

# print (f" Salom {friends[0]}, bugun choyxona bormi?\n {friends[1]}, choyxonaga boramizmi? ")

# """ t_shaxslar = ['Imom Buxoriy', 'Imom Molik']
# z_shaxslar = ['Abror Muxtor ali', 'Xusanxon Buxoriy']
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, \nzamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan suhbat qilishni istayman!") """

""" sonlar deb nomlangan ro'yxat yarating va 
ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). """

# sonlar = []

# sonlar.append(12)
# sonlar.append(-64)
# sonlar.append(18)
# sonlar.append(12.6)

# sonlar[1]= 22
# sonlar[0] = int(sonlar[0]) + 2
# misol_1 = 24 + int(sonlar[2])

# print(sonlar)

# print(misol_1)


""" friends nomli bo'sh ro'yxat tuzing va 
unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. """

friends = []

friends.append('Boburjon')
friends.append('Xurshidbek')
friends.append('Muhammadnosir')
friends.append('Sohibjon')
friends.append('Javohir')
friends.append('Muhammafyusuf')

friends.remove('Xurshidbek')

'''' Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari 
yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
mehmonlar ro'yxatiga qo'shing. ''' 


# yangi_mehmonlar = []

# yangi_mehmonlar.append(friends.pop(0))
# yangi_mehmonlar.append(friends.pop(1))
# yangi_mehmonlar.append(friends.pop(2))

# print(f"yangi mehmonlar: {yangi_mehmonlar} ")


# lstrip -> chapdan joyni olip tashlash
# rstrip -> o'ngdandan joyni olip tashlash
# strip -> bo'sh joyni olip tashlash
# .append(index) -> list ga yangi narsa qo'shish
# .insert(index) -> list dagi element o'rniga yangi narsa qo'shish!
# del ro'yxat_o'zgaruvchi[0] -> listdagi ma'lum bir [0] elementni o'chirib tashlash!
# .pop(index) -> listdan elementni sug'urib olish!


# new = ['Bob', 'Tom', 'Jack', 'Xan', 'Ali', 'Guli']

# # new.sort(reverse=True)

# new.reverse()

# # print(new)
# print (new)


# sonlar = list(range(1,11))

# juft_sonlar = list(range(0,101,2))
# toq_sonlar = list(range(1,101,2))

# print(f"Juft sonlar: {juft_sonlar[21]} , Toq sonlar: {toq_sonlar[21]}")

# narxlar = [2,200,400,500,600]

# a = min(narxlar)
# b = max(narxlar)
# c = sum(narxlar)

# # print(f"Eng kam narx: {a}, Eng ko'p narx {b}, Umummiy narx: {c}")

# print(narxlar[3:])


narxlar = (2,6,8,10)


narxlar_2 = list(narxlar)

narxlar_2.append(5)

narxlar_2.sort()

print (narxlar_2)