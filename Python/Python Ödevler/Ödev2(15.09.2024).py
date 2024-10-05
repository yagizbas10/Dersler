#1ödev
# def asal_mi(sayı):
#     if (sayı == 1):
#         return False

#     elif (sayı == 2):
#         return True

#     else:
#         for i in range(2,sayı):
#             if (sayı % i == 0):
#                 return False
#         return True

# x = int(input("Asal Mı: "))
# print(asal_mi(x))

#2.ödev
# giriş = input("Cümleniz: ")

# if giriş == giriş[::-1]:
#     print("Bu bir palindromdur")
# else:
#     print("Bu bir palindrom değildir")

#3.ödev
# def carpim(*args):
#     sonuc = 1
#     for sayi in args:
#         sonuc *= sayi
#     return sonuc

# sayilar = input("Çarpılacak sayıları aralarına boşluk koyarak girin: ")
# sayilar_listesi = list(map(int, sayilar.split()))
# print("Sonuç:", carpim(*sayilar_listesi))

#4.ödev
# def biggest(x, y, z):
#     if x >= y and x >= z:
#         print(x)
#     elif y >= x and y >= z:
#         print(y)
#     else:
#         print(z)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# biggest(a, b, c)

#5.ödev
# def ters(x):
#     return x[::-1]
# çeviri = input("Cümleniz: ")
# print(ters(çeviri))

#6.ödev
# cümle = input("Cümle: ")

# for i in cümle:
#     if i.isupper():
#         print(f"Büyük {i}")
#     elif i.islower():
#         print(f"Küçük {i}")
#     else:
#         print(f"Harf olamayan: {i}")

#7.ödev
# def rakam_carpimi(sayi):
#     sonuc = 1
#     for rakam in str(sayi):  
#         sonuc *= int(rakam)
#     return sonuc

# sayi = int(input("Bir pozitif sayı girin: "))
# print("Rakamların çarpımı:", rakam_carpimi(sayi))

#8.ödev
# def kelime_degeri(kelime):
#     toplam_deger = 0
#     for harf in kelime.lower():  
#         harf_degeri = ord(harf) - ord('a') + 1
#         toplam_deger += harf_degeri
#     return toplam_deger


# gizemli_kelime = input("Gizemli kelimeyi girin: ")
# print("Kelimenin sayı değeri:", kelime_degeri(gizemli_kelime))

#9.ödev
# print("""
# *********************
# 1) Ekleme
# 2) Silme      
# 3) Görüntüleme
# çıkış için 'q'
# **********************
# """)

# liste5 = []
# while True:
    
#     seçim = input("Seçiminiz: ")
#     if seçim == "q":
#         print("Çıkış Yapılıyor...")
#         break
#     elif seçim == "1":
#         eklenecek = input("Eklemek istediğiniz değer: ")
#         liste5.append(eklenecek)
#     elif seçim == "2":
#         silinecek = input("Silinecek: ")
#         liste5.remove(silinecek)
#     elif seçim == "3":
#         print(f"Listenin Güncel Durumu: {liste5}")
#     else:
#         print("Doğru Aralıkta değer girin")

#10.ödev
# print("""
# *******************************
#         ----MENÜ----
# 1)Köfte(240TL)
# 2)Pide(160TL)
# 3)Lahmacun(180TL)
# 4)Döner(140TL)
# 5)Pizza(200TL)
# 6)Hamburger(180TL)
# 'q' ile çıkış yapabilirsin

# *******************************
# """)
# borç = 0
# while True:
    
#     opt = input("Seçiminiz: ")
#     if opt == "q":
#         print(f"Toplam Borcunuz: {borç}TL")
#         break
#     elif opt == "1":
#         print("Siparişiniz: Köfte\nFiyat: 240TL(kdv'siz)")
#         borç += 240*118/100
#     elif opt == "2":
#         print("Siparişiniz: Pide\nFiyat: 160TL(kdv'siz)")
#         borç += 160*118/100
#     elif opt == "3":
#         print("Siparişiniz: Lahmacun\nFiyat: 180TL(kdv'siz)")
#         borç += 180*118/100
#     elif opt == "4":
#         print("Siparişiniz: Döner\nFiyat: 140TL(kdv'siz)")
#         borç += 140*118/100
#     elif opt == "5":
#         print("Siparişiniz: Pizza\nFiyat: 200TL(kdv'siz)")
#         borç += 200*118/100
#     elif opt == "6":
#         print("Siparişiniz: Hamburger\nFiyat: 180TL(kdv'siz)")
#         borç += 180*118/100
#     else:
#         print("Lütfen uygun aralıkta seçim yapın...")
