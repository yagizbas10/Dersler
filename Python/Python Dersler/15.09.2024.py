def topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam
x= topla(1,2,3,4,5,6,7)
print(x)
print(type(x))