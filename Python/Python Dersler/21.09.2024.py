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
# 1)Bakiye Sorgu
# 2)Yatırma
# 3)Çekme
# 4)Çıkış(q)
# -----------------
# """)

# sys_şifre = "9876"
# deneme = 0
# bakiye = 1000
# while deneme <3:
#     şifre = input("Şifre: ")
#     while True:    
#         if sys_şifre == şifre:
            
#             seçim = input("Seçiminiz: ")
#             if seçim == "q":
#                 print("Bankadan Çıkılıyor")
#                 break
#             elif seçim == "1":
#                 print(f"Bakiyeniz: {bakiye}TL")
#             elif seçim == "2":
#                 deposit = int(input("Yatırılacak Miktar: "))
#                 print(f"{deposit}TL Yatırılmıştır")
#                 bakiye += deposit
#             elif seçim == "3":
#                 Çekilen = int(input("Çekilecek Miktar: "))
#                 if bakiye - Çekilen < 0:
#                     print(f"Bu miktarda para çekemezsiniz\nBakiyeniz {bakiye}")
#                 else:    
#                     print(f"Bankanızdan {Çekilen}TL çekilmiştir")
#                     bakiye -= Çekilen
#             else:
#                 print("Düzgün aralıkta bir seçim yapın")
#             break
#         else:
#             print("Yanlış Şifre")
#         deneme += 1    