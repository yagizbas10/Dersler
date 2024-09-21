# 1. ödev
cümle = input("Cümleniz: ")
print(cümle.replace("","-"))

# 2. ödev
kelime = input("Kelime: ")
print(kelime.upper())

# 3. ödev
ad = input("İsminiz: ")
soyad = input("Soyadınız: ")
full_name = ad + soyad
print(f"Adınız ve soyadınızın uzunluğu {len(full_name)} harften oluşur")

# 4. ödev
ürün1= float(input("1. ürün: "))
ürün2= float(input("2. ürün: "))
ürün3= float(input("3. ürün: "))

total = ürün1 + ürün2 + ürün3
print(f"Total: {total}")

# 5. ödev
x = input("1. cümle: ")
y = input("2. cümle: ")

total = x + " " + y
print(total)

# 6. ödev
K = input("Kelimeniz: ")
harf = input("Bulmak İstediğiniz harf: ")

print(K.count(harf))

# 7. ödev
X = input("Kelime: ")
print(X.capitalize())

# 8. ödev
kücük = input("Kelimeniz: ")
print(kücük.lower())

# 9. ödev
ters = input("Adınız: ")
print(ters[::-1])

# 10. ödev
metin = input("Metniniz: ")
print(metin.strip())

# 11. ödev
kontrol = input("Cümleniz: ")
print(kontrol.isupper())

# 12. ödev
test = input("Cümleniz: ")
print(test.isalnum())