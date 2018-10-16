for a in range(1,500):
    for b in range(2,500):
        c = (a**2+b**2)**(1/2.0)
        if(a+b+c) == 1000:
            print a,b,c
