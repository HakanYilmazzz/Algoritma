asalmi = 1 #0 ise asal degildir. 1 ise asaldir.
toplam = 0
a = []
for i in range(2, 1000000) :
    for j in range(2, i) :
        if i%j == 0 :
            asalmi = 0
            break
    if asalmi == 1 :
        a.append(i)
    asalmi = 1
print a[10001]
