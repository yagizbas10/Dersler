# products = {
#     "Elma":10,
#     "Muz":5,
#     "Portakal":8
# }

# while True:
#     işlem = input("Ürün ekle (e), çıkarmak için (ç) çıkış için(q): ")
#     if işlem == "q":
#         print("Çıkış yapılıyor")
#         break
#     elif işlem == "e":
#         ürün = input("Ürün adı: ").capitalize()
#         miktar = int(input("Stok miktarı: "))
#         if ürün in products:
#             products[ürün] += miktar
#         else:
#             products[ürün]=miktar
#         print(f"{ürün} ürününün stok miktarı {products[ürün]} oldu")
#     elif işlem == "ç":
#         çıkarılan_ürün = input("Çıkarmak istediğiniz Ürün: ").capitalize()
#         çıkarılacak_miktar = int(input("Stoktan düşmek istediğiniz miktar"))
#         if çıkarılan_ürün in products and products[çıkarılan_ürün]>=çıkarılacak_miktar:
#             products[çıkarılan_ürün] -= çıkarılacak_miktar
#             if products[çıkarılan_ürün] == 0:
#                 print(f"{çıkarılan_ürün} ürünü stokta kalmadı")
#             else:
#                 print(f"{çıkarılan_ürün} ürününün stok miktarı {products[çıkarılan_ürün]}")
#         else:
#             print("Stok yok")
#     else:
#         print("Yanlış seçim")




# print("""
# ------ATM-------
# 1) Bakiye Sorgu
# 2) Yatırma
# 3) Çekme
# 4) Çıkış(q)
# -----------------
# """)

# sys_şifre = "9876"
# deneme = 0
# bakiye = 1000

# while deneme < 3:
#     şifre = input("Şifre: ")
#     if sys_şifre == şifre:
#         while True:
#             seçim = input("Seçiminiz: ")
#             if seçim == "q":
#                 print("Bankadan Çıkılıyor")
#                 break
#             elif seçim == "1":
#                 print(f"Bakiyeniz: {bakiye} TL")
#             elif seçim == "2":
#                 deposit = int(input("Yatırılacak Miktar: "))
#                 print(f"{deposit} TL Yatırılmıştır")
#                 bakiye += deposit
#             elif seçim == "3":
#                 çekilen = int(input("Çekilecek Miktar: "))
#                 if bakiye - çekilen < 0:
#                     print(f"Bu miktarda para çekemezsiniz. Bakiyeniz: {bakiye}")
#                 else:
#                     print(f"Bankanızdan {çekilen} TL çekilmiştir")
#                     bakiye -= çekilen
#             else:
#                 print("Geçerli bir seçim yapın.")
#         break  # Doğru şifre girildikten sonra dış döngüden de çık
#     else:
#         deneme += 1
#         print("Yanlış Şifre")

# if deneme == 3:
#     print("3 defa yanlış şifre girdiniz. Hesap kilitlendi.")





