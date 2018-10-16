fib_basamak = 0
fib1 = 1
fib2 = 1

for i in range(3,10000) :
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
                    
    c = fib
    while 1 :
        c = c / 10
        if c == 0 :
            break
        fib_basamak += 1

    if fib_basamak+1 == 1000 :
        print i,". fib. sayisi",fib_basamak+1," basamaklidir."
        
    fib_basamak = 0
