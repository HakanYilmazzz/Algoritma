fib = [1,1]
toplam = 0
i=2

while toplam<1000:
    fib.append(fib[i-1]+fib[i-2])
    if fib[i] == (fib[i]/2)*2:
        toplam += fib[i]
    i += 1
print i
