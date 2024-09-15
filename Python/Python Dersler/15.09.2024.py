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

# def kimlik(**kwargs):
#     return kwargs

# n = kimlik(ad= "Yağız",soyad = "Baş", yaş = 15)
# print(n)
# print(type(n))

# def deneme(*args,**kwargs):
#     return args,kwargs

# p = deneme("Django","html", 1,2,3,4,5,tc = 1111,ad="Ahmet",Soyad="Yılmaz")

# print(p)
# print(type(p))

# print(len(p))
# print(p[1],["Soyad"])
# print(p[0][4])


# def kareal(x):
#     return x**2
# print(kareal(6))


# b= lambda a: a**3
# print(b(5))


# def topla(x,y):
#     return x + y

# n = lambda x,y:x+y

# çiftmi = lambda a:"Çift" if a % 2 == 0 else "Tek"

# print(çiftmi(5))


# liste = [1,2,3,4,5,6,7,8,9,10]
# mp = map(lambda x:x**2,liste)
# print(tuple(mp))



# def uzunluk(metin):
#     return len(uzunluk)

# veri =("apple","samsung","vestel","arçelik","bosch",[1,2,3,4,5,6,7,8,9,10],{123,234,435,56,767,90,43})

# mapp = map(uzunluk,veri)
# print(tuple(mapp))

data= ["python","html","css","bootstrap","django",50,100,150,200]
def ilkharf(x):
    sonuc = str(x)[0]
    return sonuc

birleşim= map(ilkharf,data)
print(tuple(birleşim))

y = [0,1,2,3,4,5,6,7,8,9,10]

def çiftsayı(x):
    return x%2 == 0

filtre = filter(çiftsayı,y)
print(tuple(filtre))
