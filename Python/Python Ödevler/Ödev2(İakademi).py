
print("Merhaba, bu program kişisel bilgilerinizi düzenler ve formatlar.")
fullname = input("Tam adınız: ")
yaş = int(input("Yaşınız: "))
şehir = input("Yaşadığınız şehir: ")
email = input("Mailiniz: ")
hobi = input("Hobiniz: ")

fullname = fullname.title()
şehir = şehir.strip().upper()
email = email.strip()


print("************")
print(f"\nTam isim: {fullname}\n Yaş: {yaş}\n Şehir: {şehir}\n E-mail: {email}\n Hobi: {hobi}\n")
print("************")
print("Uygulamayı kullandığınız için teşekkür ederiz...")