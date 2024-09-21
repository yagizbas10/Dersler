#1.ödev
# x = "Merhaba ben Serkan"
# print(len(x))

# #2.ödev
# isim = "Serkan"
# soyisim = "ALICI"
# print("Benim ismim {} {}".format(isim,soyisim))

# #3.ödev
# splitter = "Benim ismim Serkan ALICI"
# new = splitter.split(" ")
# print(new)

#4.ödev
# liste = ["ömer",34,56,78,90,[4,5,6],89]
# liste.append("ali")
# print(liste)
# print(liste[4])

#5.ödev
# rakamlar = [4, 6, 3, 8, 1, 0]
# rakamlar.sort()  
# print(rakamlar)

#6.ödev
# sözlük = {
#     "ali" : 34,
#     "ahmet": 35,
#     "kemal" : 45,
#     "mustafa" : 55
# }
# anahtarlar = sözlük.keys()
# değerler = sözlük.values()
# print(f"Anahtarlar: {anahtarlar}\nDeğerler: {değerler}")

#7.ödev
# def küpalma(x):
#     return x**3

# print(küpalma(4))

#8.ödev
# a = 0
# while a<10:
#     print(a)
#     a +=1

#9.ödev
# for i in range(0,101,5):
#     print(i)

#10.ödev
# ad = input("Ad: ")
# yaş = int(input("Yaş: "))
# yüzyılyaş=100 - yaş
# print(f"{ad}, {yüzyılyaş} yıl sonra 100 yaşına gireceksin")

#11.ödev
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(f"İstenen Sayı: {i}")

#12.ödev

# kullanici_ismi = input("Kullanıcı ismi girin: ")

# if kullanici_ismi == "admin":
#     baslangic = int(input("Başlangıç değerini girin: "))
#     bitis = int(input("Bitiş değerini girin: "))
#     artis = int(input("Artış değerini girin: "))

#     for i in range(baslangic, bitis + 1, artis):
#         print(i)

# elif kullanici_ismi == "uye":
#     bitis = int(input("Bitiş değerini girin: "))
#     baslangic = 1
#     artis = 1
    
#     for i in range(baslangic, bitis + 1, artis):
#         print(i)
# else:
#     print("Geçersiz kullanıcı ismi.")

#13.ödev
# yazi = "Python üst düzey basit söz dizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir dildir."
# sesliler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
# toplam_sayi = 0

# for sesli in sesliler:
#     sayi = yazi.count(sesli)
#     toplam_sayi += sayi
#     print(f"{sesli} seslisi: {sayi} kez")

# print(f"Toplam sesli sayısı: {toplam_sayi}")

#14.ödev
# max_email_attempts = 3
# max_password_attempts = 5
# email_attempts = 0
# password_attempts = 0

# while email_attempts < max_email_attempts:
#     email = input("Enter your email address: ").strip()
#     if email == "":
#         print("Email cannot be empty!")
#         continue
    
#     if "@" in email:
#         break
#     else:
#         email_attempts += 1
#         print(f"Invalid email address! You have {max_email_attempts - email_attempts} attempts left.")
    
# if email_attempts == max_email_attempts:
#     print("Too many invalid email attempts. Exiting...")

# else:
#     while password_attempts < max_password_attempts:
#         password = input("Enter your password: ").strip()
#         if password == "":
#             print("Password cannot be empty!")
#             continue
        
#         if password[0].isupper() and len(password) >= 8:
#             print("Login successful!")
#             break
#         else:
#             password_attempts += 1
#             print(f"Invalid password! You have {max_password_attempts - password_attempts} attempts left.")
    
#     if password_attempts == max_password_attempts:
#         print("Too many invalid password attempts. Exiting...")

#15.ödev
# kilo = input("Kargonuz kaç kilodur: ").replace(",", ".")
# teslimat_tutarı = 0


# if kilo.replace(".", "", 1).isdigit() and 0.1 <= float(kilo) <= 50:  
#     kilo = float(kilo)
#     if 0.1 <= kilo <= 2:
#         teslimat_tutarı += 10
#     elif 2 < kilo <= 6:
#         teslimat_tutarı += 9
#     elif 6 < kilo <= 10:
#         teslimat_tutarı += 8
#     elif 10 < kilo <= 20:
#         teslimat_tutarı += 7
#     elif 20 < kilo <= 50:
#         teslimat_tutarı += 6
#     print(f"Teslimat Tutarınız: {teslimat_tutarı} TL")
# else:
#     print("Lütfen uygun aralıkta bir ağırlık giriniz.")

#16.ödev

# sözlük2 = {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25,
#     6: 36,
#     7: 49,
#     8: 64
# }

# n = int(input("Bir tam sayı girin: "))

# yeni_sözlük = {}

# for i in range(1, n + 1):
#     yeni_sözlük[i] = i ** 2

# print(yeni_sözlük)

# 17.ödev
# liste3 = []
# while True:
#     giriş = input("Bir değer giriniz: ")

#     if giriş == "":
#         print(liste3)
#         break
#     else:
#         liste3.append(giriş)

#18.ödev
# for num in range(1000, 3001):
#     # Sayıyı string'e çeviriyoruz ve her basamağını kontrol ediyoruz
#     if all(int(digit) % 2 == 0 for digit in str(num)):
#         print(num)