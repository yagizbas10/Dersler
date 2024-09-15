# differance (a,b) (a kümesinin b kümesinden farklı elemanları)
# a = {3,6,9,12,15}
# b = {22,6,9,2,1}

# print(a.difference(b))
# print(b.difference(a))

# #intersection (a kesişim b)
# print(a.intersection(b))

# # union
# print(a.union(b))

# #copy (kopyalama)
# kopya_a = a.copy
# print(kopya_a)

# #clear
# kopya_a.clear()
# print(kopya_a)

#liste tuple sözlük küme dönüşümü

# 
# tuple: tuple(x)
# set: set(x)
# list: list(x)
# dict: dict{
#     Key:Value
# }


# dictionaries(sözlükler)

# sözlük = {
#     "ad":"Yağız",
#     "soyad": "Baş",
#     "yaş": 15,
#     "email": "yagizbas10@gmail.com",
#     "adres": "İzmir/Alsancak"
# }

# print(sözlük)
# print(type(sözlük))
# print(len(sözlük))

# print(sözlük["ad"])

# ad = input("Ad: ")
# soyad = input("Soyad: ")
# no = int(input("Öğrenci no: "))
# dönem = int(input("Dönem: "))
# email = input("Mail: ")
# telefon = input("Telefon: ")
# Bilgiler = [email,telefon]
# dersad = input("Ders Adı: ")
# derskodu = input("Ders Kodu: ")
# dershocası = input("Ders Hocası: ")


# öğrenci = {
#     "ad": ad,
#     "soyad": soyad,
#     "Öğrenci no": no,
#     "Bilgiler": Bilgiler,
#     "Dönem": dönem,
#     "Ders Bilgileri": {
#         "Ders kodu":derskodu,
#         "Ders adı":dersad,
#         "Ders hocası":dershocası
#     }
# }

# print(öğrenci)

# dict.keys(): Anahtar değerleri bulur
# dict.values(): Değerleri bulur
# dict.items(): Anahtar ve Değerleri Tuple şeklinde bulur
# dict.get("ad"): dict["ad"] ile eşittir
# dict.update({
#   "adres": "İzmir",
#   "ilçe": "Konak" 
#      })
# dict.pop: parametre olarak firilen anahtar ismi ve değerini siler
# del: anahtar ismiyle silme işlemi yapar
# popitem: sözlüğün son elemanını siler
# sorted(öğrenci)
# if koşul:
#    kod

# sıcaklık = int(input("Sıcaklık girin: "))
# if sıcaklık <= 30: 
#     print("Hava normal")
# else:
#     print("Hava sıcak")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# sys_username = "admin"
# sys_password = "123"

# if username == sys_username and password == sys_password:
#     print("Login successful...")
# elif username == sys_username and password != sys_password:
#     print("Password incorrect")
# elif username != sys_username and password == sys_password:
#     print("Username incorrect")
# else:
#     print("Username and Password is incorrect")


# note = (input("Notunuz: "))
# if note.lstrip('-').isnumeric()==True:
#     note = float(note)
#     if note<0:
#         print("Positif sayı girin")
#     elif 0 <= note <= 100:
#         if note >= 90:
#             print("AAA")
#         elif 80 <= note <90:
#             print("AA")
#         elif 70 <= note < 80:
#             print("BB")
#         elif 60 <= note < 70:
#             print("CC")
#         elif 50 <= note < 60:
#             print("DD")
#         else:
#             print("FF") 
#     else:
#         print("Lütfen doğru aralıkta not girin")
# else:
#     print("Lütfen harf yerine sayı kullanın")

# liste = ["hello","World"]
# for i in liste:
#     print(i)

# b= {1,2,3,4,5,6,7}
# for i in b:
#     print(i)

# sözlük = {
#     "ad":"Yağız",
#     "soyad": "Baş",
#     "yaş": 15,
#     "email": "yagizbas10@gmail.com",
#     "adres": "İzmir/Alsancak"
# }

# for i in sözlük:
#     print(i,sözlük[i])


# x = 2005
# for i in x:
#     print(i)


# numeric sayılar iterable DEĞİLDİR




