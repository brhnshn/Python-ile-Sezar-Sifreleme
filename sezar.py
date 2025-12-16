alfabe = "abcdefghijklmnopqrstuvwxyz"

metin = input("Metni gir: ")
kaydirma = int(input("Kaydırma sayısını gir: "))

sonuc = ""

for h in metin:
    if h in alfabe:
        sonuc += alfabe[(alfabe.index(h) + kaydirma) % 26]
    else:
        sonuc += h

print(sonuc)
