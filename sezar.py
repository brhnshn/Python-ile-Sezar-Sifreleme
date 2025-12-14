metin = input("Metni girin: ")
sayi = int(input("Kaydırma sayısı: "))
sonuc = ""

for harf in metin:
    if harf.isalpha():
        # Büyük harfse 'A'(65), küçükse 'a'(97) baz alınır
        baslangic = 65 if harf.isupper() else 97
        
        # Matematiksel formül (Mod alma işlemi)
        yeni_kod = (ord(harf) - baslangic + sayi) % 26 + baslangic
        sonuc += chr(yeni_kod)
    else:
        sonuc += harf

print("Çıktı:", sonuc)