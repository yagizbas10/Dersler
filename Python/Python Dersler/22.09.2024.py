# students = []
# while True:
#     ad = input("(Çıkış = q) Öğrenci Adını girin: ")
#     if ad == "q":
#         break
#     notlar = list(map(int, input("Öğrencinin notları: ").split()))
#     students.append({
#         "ad": ad,
#         "notlar": notlar
#     })

# aranan_isim = input("Not ortalamasını görmek istediğiniz öğrencinin adını giriniz: ")

# # Öğrenciyi bul ve ortalamasını hesapla
# bulundu = False
# for i in students:
#     if i["ad"] == aranan_isim:
#         ort_not = sum(i["notlar"]) / len(i["notlar"])
#         print(f"{aranan_isim} adlı öğrencinin not ortalaması: {ort_not:.2f}")
#         bulundu = True
#         break

# if not bulundu:
#     print(f"{aranan_isim} adlı öğrenci bulunamadı.")

#*****************************************************
# Yıllık = []
# for i in range(1,13):
#     ay = int(input(f"{i}.Ay birikim miktarınız: "))
#     Yıllık.append(ay)

# toplam = sum(Yıllık)

# if toplam >= 100000:
#     print(f"Yıllık istenen miktara ulaştınız.Miktar: {toplam}")
# elif toplam < 0:
#     print(f"{toplam}TL borçtasınız")
# else:
#     print(f"Yıllık hedefe ulaşamadınız. Biriken miktar: {toplam}")

#*************************************************************


#########################   DECORATORS   #################################

import time
import math
def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):
        başlangıç = time.time() #şuan ki saat
        fonk(*args,**kwargs)
        bitiş = time.time()
        return f"İşlem {bitiş-başlangıç} saniyede tamamlanmıştır."
    return wrapper

@zaman_hesapla
def üs_al(x,y):
    time.sleep(1)
    return pow(x,y)

@zaman_hesapla
def topla(a,b):
    return a+b

@zaman_hesapla
def küp_al(d):
    for i in d:
        sonuç = i**3
    return sonuç

print(üs_al(2,5))
print(küp_al(range(1,21)))
print(topla(5,2))