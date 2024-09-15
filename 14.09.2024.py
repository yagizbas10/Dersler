# print("""
# *************************************
# 1) Toplama
# 2) Çıkarma
# 3) Çarpma
# 4) Bölme
# 5) Kuvvet
# 6) Karekök
# çıkmak için 'q' ya basın
# *************************************      
# """)
# seçim = input("Bir seçenek seçin lütfen: ")
# while True:
#     x = float(input("x: "))
#     y = float(input("y: "))
#     if seçim == "q":
#         print("Çıkış yapılıyor")
#         break
#     elif seçim == "1":
#         print(f"Toplam: {x+y}")
#     elif seçim == "2":
#         print(f"Çıkartma: {x-y}")
#     elif seçim == "3":
#         print(f"Çarpım: {x*y}")
#     elif seçim == "4":
#         if y != 0:
#             print(f"Bölüm: {x/y}")
#         else:
#             print("Hiçbir sayı sıfıra bölünemez")
#     elif seçim == "5":
#         print(f"Üs: {x**y}")
#     elif seçim == "6":
#         print(f"x'in kökü: {x**0.5}\ny'nin kökü: {y**0.5}")
#     else:
#         print("Lütfen doğru bir giriş yapın")

# for i in range(5,21):
#     print(i)

# liste = [list(range(0,11)),list(range(50,81)),list(range(150,221))]
# print(liste)
# print(liste[1][-1])


# for i in range(0,3):
#     şifre = input("şifre tanımlayın: ")
#     if not şifre: #şifre boşsa
#         print("Şifee boş geçilmez")
#     elif len(şifre) in range(3,9):
#         print(f"Şirfeniz Tanımlanmıştır\nŞifreniz: {şifre}")
#         break
#     elif i==2:
#         print("Hakkınız bitti")
#     else:
#         print("Şifre uzunluğu 3-8 aralığında olmalı")


#Parametreli Fonkisyonlar

# def bilgiler(ad,soyad,yaş):
#     ad = ad.lower().capitalize().replace(" ","")
#     soyad = soyad.lower()
#     şifre =  ad + soyad + yaş
#     return şifre

# isim=input("İsim: ")
# soyisim=input("Soyisim: ")
# yaşş=input("yaşş: ")
# print(bilgiler(isim,soyisim,yaşş))


def çiftmi(sayi):
    if sayi%2 == 0:
        return f"{sayi} sayısı çift sayıdır"
    else:
        return f"{sayi} sayısı çift sayı değildir"

print(çiftmi(22))
