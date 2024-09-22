import math
import random
# print(math.sqrt(25))
# print(math.perm(5,2))
# print(math.floor(4.6))
# print(math.comb(8,2))

# #**********************************************************


# print(random.randint(0,20))
# print(random.random())
# liste = ["İzmir","Aydın","İstanbul"]
# sehir = random.choice(liste)
# print(sehir)

# print(random.uniform(5,10))
# print(random.randrange(3,9))
# h = []
# for i in range(0,10):
#     h.append(random.randrange(0,100,3))
# print(h)
#***********************************

# a=random.randint(0,100)
# deneme = 0

# while True:
#     tahmin = int(input("Tahmininiz: "))
#     if a == tahmin:
#         print(f"{tahmin} Sayısı istenilen sayıydı")
#         print(f"{deneme}. denemede doğru tahmin")
#         break
#     else:
#         if a>tahmin:
#             print("Daha büyük girin")
#         else:
#             print("Daha küçük girin")
#         deneme += 1


#********************************
# mesafe = float(input("Gideceğiniz Km: "))
# başlangıç = 40.0
# km_başına= 3.5
# ücret = başlangıç + mesafe*km_başına

# if mesafe >50:
#     ücret = ücret * 0.9

# print(f"Toplam ücret: {ücret}TL")


#***********************************

sayi = int(input("Sayı giriniz: "))
for i in range(1,11):
    print(f"{sayi} x {i} = {sayi*i}")