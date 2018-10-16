def basamak_degeri_topla(sayi):
    deger = 0
    while sayi:
        basamak = sayi % 10
        sayi = sayi / 10
        deger += basamak
    print deger

m = input("faktoriyeli alinacak sayi: ")

fak = 1

for i in range(1,m+1):
    fak = fak*i
print fak

basamak_degeri_topla(fak)
