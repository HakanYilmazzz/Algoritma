import random

kontrol = True
sayac = 0

while kontrol:
    rastgele_sayi = random.randint(1,100)
    if rastgele_sayi == 42:
        kontrol=False
    sayac = sayac + 1

print sayac, " denemede hedefe ulasildi"