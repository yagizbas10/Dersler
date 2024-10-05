#1.ödev
# def toplam_butce_kontrolu(hediye_listesi, toplam_butce):
#     toplam_gider = sum(butce for isim, butce in hediye_listesi)
    
#     if toplam_gider <= toplam_butce:
#         return True, toplam_gider
#     else:
#         return False, toplam_gider

# hediye_listesi = []
# print("Hediye listesine isim ve bütçeleri girin (çıkmak için 'q' tuşuna basın):")

# while True:
#     isim = input("İsim: ")
#     if isim.lower() == 'q':
#         break
#     butce = float(input(f"{isim} için bütçe: "))
#     hediye_listesi.append((isim, butce))


# toplam_butce = float(input("Toplam bütçe: "))

# alınabilir_mi, toplam_gider = toplam_butce_kontrolu(hediye_listesi, toplam_butce)
# if alınabilir_mi:
#     print(f"Toplam bütçeyi aşmadan hediye alınabilir. Toplam gider: {toplam_gider}")
# else:
#     print(f"Toplam bütçeyi aşıyor. Toplam gider: {toplam_gider}")

#2.ödev
# def rezervasyon_ucreti_hesapla(baslangic_gunu, bitis_gunu, kisi_sayisi, gunluk_ucret):
#     # Toplam gün sayısını hesapla
#     toplam_gun = bitis_gunu - baslangic_gunu
    
#     # Toplam ücreti hesapla
#     toplam_ucret = toplam_gun * kisi_sayisi * gunluk_ucret
    
#     # 3 günden uzun ise %10 indirim uygula
#     if toplam_gun > 3:
#         toplam_ucret *= 0.9  # %10 indirim
    
#     return toplam_ucret

# # Kullanıcıdan giriş al
# baslangic_gunu = int(input("Rezervasyon başlangıç gününü girin (örnek: 1-30): "))
# bitis_gunu = int(input("Rezervasyon bitiş gününü girin (örnek: 1-30): "))
# kisi_sayisi = int(input("Kişi sayısını girin: "))
# gunluk_ucret = float(input("Günlük ücreti girin: "))

# # Ücreti hesapla
# toplam_ucret = rezervasyon_ucreti_hesapla(baslangic_gunu, bitis_gunu, kisi_sayisi, gunluk_ucret)

#3.ödev
# def ceza_hesapla(hiz_limiti, arac_hizi):
#     # Hız aşımı hesapla
#     hiz_asimi = arac_hizi - hiz_limiti

#     # Ceza miktarını başlangıçta sıfır olarak tanımla
#     ceza = 0
    
#     # Hız limitinin 20 km/saat üstüne çıkanlar için 100 TL ceza
#     if 20 < hiz_asimi <= 40:
#         ceza = 100
    
#     # Hız limitinin 40 km/saat üstüne çıkanlar için 250 TL ceza
#     elif hiz_asimi > 40:
#         ceza = 250
    
#     return ceza

# # Kullanıcıdan giriş al
# hiz_limiti = int(input("Hız limitini girin (km/saat): "))
# arac_hizi = int(input("Aracın hızını girin (km/saat): "))

# # Ceza hesapla
# ceza = ceza_hesapla(hiz_limiti, arac_hizi)

# if ceza > 0:
#     print(f"Ceza miktarı: {ceza} TL")
# else:
#     print("Hız limitini aşmadınız, ceza yok.")

#4.ödev
# def luhn_kontrol(kart_numarasi):
#     # Kart numarasını ters çevirip rakamları ayır
#     kart_numarasi = [int(x) for x in str(kart_numarasi)][::-1]
    
#     toplam = 0
    
#     # Her ikinci basamağı çiftleyip toplamı hesapla
#     for i, rakam in enumerate(kart_numarasi):
#         if i % 2 == 1:
#             ciftlenmis = rakam * 2
#             if ciftlenmis > 9:
#                 ciftlenmis -= 9
#             toplam += ciftlenmis
#         else:
#             toplam += rakam
    
#     # Sonucun 10 ile bölünüp bölünmediğini kontrol et
#     return toplam % 10 == 0

# # Kullanıcıdan kart numarasını al
# kart_numarasi = input("Kredi kartı numarasını girin: ")

# # Kartın geçerli olup olmadığını kontrol et
# if luhn_kontrol(kart_numarasi):
#     print("Kart numarası geçerlidir.")
# else:
#     print("Kart numarası geçersizdir.")

#5.ödev
# def yatirim_karsilastir(yatirimlar, miktar, yil):
#     kazanc_sonuclari = {}
    
#     # Her yatırım türü için yıllık geri dönüş oranlarını kullanarak kazancı hesapla
#     for yatirim_turu, oran in yatirimlar.items():
#         # Geri dönüş oranını kullanarak belirli bir yıl sonrasındaki kazancı hesapla
#         kazanc = miktar * ((1 + oran) ** yil)
#         kazanc_sonuclari[yatirim_turu] = kazanc
    
#     # En yüksek kazancı sağlayan yatırımı bul
#     en_kazanc_yatirimi = max(kazanc_sonuclari, key=kazanc_sonuclari.get)
    
#     # Sonuçları göster
#     print("Yatırım türlerine göre kazançlar:")
#     for yatirim_turu, kazanc in kazanc_sonuclari.items():
#         print(f"{yatirim_turu}: {kazanc:.2f} TL")
    
#     print(f"\nEn kazançlı yatırım: {en_kazanc_yatirimi} ({kazanc_sonuclari[en_kazanc_yatirimi]:.2f} TL)")
    
# # Yatırım türleri ve yıllık geri dönüş oranları
# yatirimlar = {
#     "Borsa": 0.12,    # %12 yıllık geri dönüş
#     "Altın": 0.08,    # %8 yıllık geri dönüş
#     "Gayrimenkul": 0.07,  # %7 yıllık geri dönüş
#     "Döviz": 0.05     # %5 yıllık geri dönüş
# }

# # Kullanıcıdan giriş al
# miktar = float(input("Yatırım miktarını girin (TL): "))
# yil = int(input("Yatırım süresini girin (yıl): "))

# # Yatırım türlerini karşılaştır
# yatirim_karsilastir(yatirimlar, miktar, yil)

#6.ödev
# def dis_borc_hesapla(baslangic_borcu, *artis_oranlari):
#     borc = baslangic_borcu
#     yil = 1
    
#     # Her yıl için borç artışını hesapla
#     for oran in artis_oranlari:
#         borc += borc * oran
#         print(f"{yil}. yıl borç miktarı: {borc:.2f} TL")
#         yil += 1
    
#     return borc

# # Kullanıcıdan giriş al
# baslangic_borcu = float(input("Başlangıç borç miktarını girin (TL): "))
# yil_sayisi = int(input("Yıl sayısını girin: "))

# # Her yıl için artış oranlarını al
# artis_oranlari = []
# for i in range(yil_sayisi):
#     oran = float(input(f"{i+1}. yıl için artış oranını girin (örnek: %5 için 0.05): "))
#     artis_oranlari.append(oran)

# # Dış borcu hesapla
# toplam_borc = dis_borc_hesapla(baslangic_borcu, *artis_oranlari)

# print(f"\nToplam dış borç: {toplam_borc:.2f} TL")

#7.ödev
# def sifreleme_sistemi(anahtar):
#     # Closure fonksiyonu: Şifreleme ve çözme işlemleri burada yapılacak
#     def sifrele(metin):
#         # Şifreleme: Her harfi anahtar kadar ileri kaydır
#         sifreli_metin = ''.join([chr((ord(harf) + anahtar - 65) % 26 + 65) if harf.isupper() else
#                                  chr((ord(harf) + anahtar - 97) % 26 + 97) if harf.islower() else harf
#                                  for harf in metin])
#         return sifreli_metin

#     def coz(metin):
#         # Çözme: Her harfi anahtar kadar geri kaydır
#         cozulmus_metin = ''.join([chr((ord(harf) - anahtar - 65) % 26 + 65) if harf.isupper() else
#                                   chr((ord(harf) - anahtar - 97) % 26 + 97) if harf.islower() else harf
#                                   for harf in metin])
#         return cozulmus_metin

#     # Şifreleme ve çözme fonksiyonlarını döndür
#     return sifrele, coz

# # Kullanıcıdan giriş al
# metin = input("Şifrelenecek metni girin: ")
# anahtar = int(input("Şifreleme anahtarını girin (bir sayı): "))

# # Şifreleme sistemini başlat
# sifrele, coz = sifreleme_sistemi(anahtar)

# # Metni şifrele ve göster
# sifreli_metin = sifrele(metin)
# print(f"Şifreli metin: {sifreli_metin}")

# # Şifreli metni çöz ve göster
# cozulmus_metin = coz(sifreli_metin)
# print(f"Çözülmüş metin: {cozulmus_metin}")

#8.ödev

# def kredi_basvuru_sistemi(**bilgiler):
#     # Gerekli bilgileri kwargs ile al
#     isim = bilgiler.get("isim", "Bilinmiyor")
#     yas = bilgiler.get("yas", 0)
#     kredi_puani = bilgiler.get("kredi_puani", 0)
#     aylik_gelir = bilgiler.get("aylik_gelir", 0)
#     kredi_miktari = bilgiler.get("kredi_miktari", 0)
    
#     # Kredi uygunluğu kriterleri
#     uygun = True
#     nedenler = []
    
#     if yas < 18:
#         uygun = False
#         nedenler.append("Yaş 18'den küçük")
    
#     if kredi_puani < 600:
#         uygun = False
#         nedenler.append("Kredi puanı 600'den düşük")
    
#     # Kredi miktarı, aylık gelirin 10 katından fazla ise uygun değil
#     if kredi_miktari > aylik_gelir * 10:
#         uygun = False
#         nedenler.append(f"Kredi miktarı aylık gelirin 10 katından fazla (Aylık Gelir: {aylik_gelir}, İstenilen Kredi: {kredi_miktari})")
    
#     # Sonuçları döndür
#     if uygun:
#         return f"{isim}, kredi başvurunuz kabul edildi!"
#     else:
#         return f"{isim}, kredi başvurunuz reddedildi. Nedenler: {', '.join(nedenler)}"

# # Kullanıcıdan bilgiler al
# bilgiler = {
#     "isim": input("İsminizi girin: "),
#     "yas": int(input("Yaşınızı girin: ")),
#     "kredi_puani": int(input("Kredi puanınızı girin: ")),
#     "aylik_gelir": float(input("Aylık gelirinizi girin: ")),
#     "kredi_miktari": float(input("Talep ettiğiniz kredi miktarını girin: "))
# }

# # Kredi başvurusunu değerlendir
# sonuc = kredi_basvuru_sistemi(**bilgiler)
# print(sonuc)

#9.ödev

# def sesli_harf_say(metin):
#     sesli_harfler = "aeiouAEIOU"
    
#     # Lambda ve filter kullanarak yalnızca sesli harfleri filtrele
#     sesli_harf_listesi = list(filter(lambda harf: harf in sesli_harfler, metin))
    
#     # Sesli harfleri ve sayısını döndür
#     sesli_harf_sayisi = len(sesli_harf_listesi)
#     return sesli_harf_listesi, sesli_harf_sayisi

# # Kullanıcıdan metin al
# metin = input("Metni girin: ")

# # Sesli harfleri filtrele ve sayısını hesapla
# sesli_harfler, sayi = sesli_harf_say(metin)

# # Sonuçları ekrana yazdır
# print(f"Sesli harfler: {', '.join(sesli_harfler)}")
# print(f"Toplam sesli harf sayısı: {sayi}")

