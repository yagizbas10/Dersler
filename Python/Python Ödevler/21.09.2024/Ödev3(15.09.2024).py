def toplam_butce_kontrolu(hediye_listesi, toplam_butce):
    toplam_gider = sum(butce for isim, butce in hediye_listesi)
    
    if toplam_gider <= toplam_butce:
        return True, toplam_gider
    else:
        return False, toplam_gider

# Kullanıcıdan isimler ve bütçeleri toplamak
hediye_listesi = []
print("Hediye listesine isim ve bütçeleri girin (çıkmak için 'q' tuşuna basın):")

while True:
    isim = input("İsim: ")
    if isim.lower() == 'q':
        break
    butce = float(input(f"{isim} için bütçe: "))
    hediye_listesi.append((isim, butce))

# Toplam bütçeyi al
toplam_butce = float(input("Toplam bütçe: "))

# Fonksiyonu çağır ve sonucu yazdır
alınabilir_mi, toplam_gider = toplam_butce_kontrolu(hediye_listesi, toplam_butce)
if alınabilir_mi:
    print(f"Toplam bütçeyi aşmadan hediye alınabilir. Toplam gider: {toplam_gider}")
else:
    print(f"Toplam bütçeyi aşıyor. Toplam gider: {toplam_gider}")