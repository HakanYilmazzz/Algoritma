deger = 0

for j in range(1,100000000):
    for i in range(1,21): #20 icin denedigimizde cok fazla zaman alacagi icin sonucu vermiyor.
        if j%i == 0:
            deger += 1
        else:
            break

    if deger == 20: #daha kucuk rakamlar ile denerseniz onlarin ciktisini veriyor.
        print j
        break
    else:
         deger = 0
