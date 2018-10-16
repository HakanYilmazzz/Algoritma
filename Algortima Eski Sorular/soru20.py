n = input("limit degeri giriniz: ")
f1, f2 = 1, 1
fib = 0
toplam = 0

for i in range(2, n):
    fib = f1+f2
    f1,f2 = f2, fib

for i in str(fib):
    toplam = toplam + int(i)

print fib, toplam
