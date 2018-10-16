m = []
a = []
eklenecek = 1

for i in range(10):
    h = int(raw_input("Diziye 10 eleman girin: "))
    m.append(h)

print "Dizi: ",m

for i in range(len(m)):
    for j in range(i+1,len(m)):
        if m[i] > m[j] :
            enbuyuk = m[i]
            m[i] = m[j]
            m[j] = enbuyuk
print "Siralanmis: ",m

for k in range(len(m)):
    for l in range(len(a)):
        if int(m[k]) == int(a[l]) :
            eklenecek = 0
        
    if eklenecek == 1:
        a.append(m[k])

    eklenecek =1

print "Son hal: ",a
