# def topla(*args):
#     toplam = 0
#     for i in args:
#         toplam += i
#     return toplam
# x= topla(1,2,3,4,5,6,7)
# print(x)
# print(type(x))

# def yaz(*args):
#     return args


#Local Global değişkenleri

# def Vücütkitleindeks(kilo,boy):
#     sonuc = kilo / boy**2
#     sonuc2 = kilo/boy
#     return sonuc,sonuc2

# a = int(input("Boyunuzu giriniz: "))
# b = float(input("Kilonuzu giriniz: "))

# m = Vücütkitleindeks(a,b)
# print(m)

def kimlik(**kwargs):
    return kwargs

n = kimlik(ad= "Yağız",soyad = "Baş", yaş = 15)
print(n)
print(type(n))