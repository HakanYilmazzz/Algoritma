# Kod üzerinden akış şemasına çevrilebilir.
def P(n):
        kactane = 0
        asalmi = 1
        for i in range(2,n+1):
                for j in range(2,i):
                        if i%j == 0:
                                asalmi = 0
                                break
                if asalmi == 1:
                        kactane += 1
                asalmi = 1
        print kactane

sayi = input("Sayi girin:")

P(sayi)
