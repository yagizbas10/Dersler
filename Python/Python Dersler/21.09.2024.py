products = {
    "Elma":10,
    "Muz":5,
    "Portakal":8
}

while True:
    işlem = input("Ürün ekle (e), çıkarmak için (ç) çıkış için(q): ")
    if işlem == "q":
        print("Çıkış yapılıyor")
        break
    elif işlem == "e":
        ürün = input("Ürün adı: ").capitalize()
        miktar = int(input("Stok miktarı: "))
        if ürün in products:
            products[ürün] += miktar
        else:
            products[ürün]=miktar
        print(f"{ürün} ürününün stok miktarı {products[ürün]} oldu")
    elif işlem == "ç":
        çıkarılan_ürün = input("Çıkarmak istediğiniz Ürün: ").capitalize()
        çıkarılacak_miktar = int(input("Stoktan düşmek istediğiniz miktar"))
        if çıkarılan_ürün in products and products[çıkarılan_ürün]>=çıkarılacak_miktar:
            products[çıkarılan_ürün] -= çıkarılacak_miktar
            if products[çıkarılan_ürün] == 0:
                print(f"{çıkarılan_ürün} ürünü stokta kalmadı")
            else:
                print(f"{çıkarılan_ürün} ürününün stok miktarı {products[çıkarılan_ürün]}")
        else:
            print("Stok yok")
    else:
        print("Yanlış seçim")