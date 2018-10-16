asalmi = 1 
toplam = 0

for i in range(2, 2000000) :
    for j in range(2, i) : 
        if i%j == 0 :
            asalmi = 0
            break 
    if asalmi == 1 :
        toplam += i
    asalmi = 1
print "2000000 dan kucuk asal sayilarin toplami ",toplam,"dir."
