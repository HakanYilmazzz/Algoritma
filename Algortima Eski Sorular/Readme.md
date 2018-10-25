Algoritma Eski Sorular ve Çözümleri
==================================
<h4>Çanakkale On Sekiz Mart Üniversitesi Bilgisayar Mühendisliği</h4>
<h5>Algoritma ve Programlama Dersi<h5> 


 Necdet hocanın önceki yıllarda sorduğu soruları ve çözümlerini içeren bir döküman
 
 

**SORU 1** ) 2^1000 ’nin basamak değerleri toplamını bulan bir python kodu yazınız. 

İpucu:   Örneğin   2^15 ’in   değeri   32768   olduğundan   soru   1000   yerine   15   için   sorulsaydı  
cevap 3 + 2 + 7 + 6 + 8 = 26 olurdu.

> Soru1.py

```
def basamak_degeri_topla(sayi):
  deger = 0
  while sayi:
    basamak = sayi % 10
    sayi = sayi / 10
    deger += basamak
  print deger

carpim = 1

for i in range(1000):
    carpim = carpim*2 

print carpim

basamak_degeri_topla(carpim) 
```


**Soru 2)** Eğer bir sayı kadar nokta kullanılarak bir üçgen oluşturulabiliyorsa o sayıya 
üçgen sayı denmektedir. İlk altı üçgen sayı (1,3,6,10,15,21) aşağıda gösterilmektedir. Buna 
göre kullanıcıdan okuduğu sayının bir üçgen sayı olup olmadığını belirleyen bir python 
programı yazınız. 

>Soru2.py

```
m = input("Sayiyi girin: ")

toplam = 0
ucgen_sayi = 0

for i in range(m+1):
    toplam += i
    if toplam == m:
        print m,"sayisi ucgen sayidir."
        ucgen_sayi=1
if ucgen_sayi == 0:
print m,"Ucgen sayi degildir."
```



**Soru 3)** 10 elemanlı ve elamanları tekrar edebilen biri dizinin elemanlarını 
tekrarsız bir şekilde sıralayan algoritmayı yazınız. İstediğiniz sıralama algoritmasını 
kullanabilirsiniz. 
      Örnek: {3,42,1,3,17,1,1,1,10,2} -> {1,2,3,10,17,42}

>Soru3.py

```
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
```

**Soru 4)** Sadece çift Fibonacci sayılarını toplayarak 1000'i geçmeye çalışıyorsunuz. En son kaçıncı 
Fibonacci sayısı bu diziye dahil olacaktır?

>Soru4.py

```
fib = [1,1]
toplam = 0
i=2

while toplam<1000:
    fib.append(fib[i-1]+fib[i-2])
    if fib[i] == (fib[i]/2)*2:
        toplam += fib[i]
    i += 1
print i
```

**Soru 5) **a < b < c  olmak üzere  a^2 + b^2 = c^2  olan tam sayılara Pisagor üçlüsü denir.  a + b + c = 1 000
olacak şekilde tek bir Pisagor üçlüsü vardır. Onu bulmanız istenmektedir.

>Soru5.py

```
for a in range(1,500):
    for b in range(2,500):
        c = (a**2+b**2)**(1/2.0)
        if(a+b+c) == 1000:
print a,b,c
```


**Soru 6)** Elinizde 1, 2, 5, 10, 25 ve 50 kuruşluk madeni paralarınız olsun. Bu paraları kullanarak 
toplamda 1 TL olusturmanız istenmektedir. Her seferinde her madeni para türünden mutlaka 
kullanmanız gerekmiyorsa kaç farklı şekilde 1 TL elde edilebildiğini hesaplayınız.

>Soru6.py

```
cevap = 0

for a in range(0,101):
    for b in range(0,51):
        for c in range(0,21):
            for d in range(0,11):
                for e in range(0,5):
                    for f in range(0,3):
                        if a+2*b+5*c+10*d+25*e+50*f == 100:
                            cevap += 1
print cevap

```



**Soru 7)** NxN’lik bir kare üzerinde en fazla kaç kare bulunduğunu hesaplayan programın 
akış şemasını çiziniz. (Örneğin 2x2’lik bir kare üzerinde 5 kare bulunabilir) 

>Soru7.py

```
m = input("kaca kaclik kare?: ")

kare = 0

for i in range(1,m+1):
    kare += i*i

print kare
```

**Soru 8)** Kaçıncı Fibonacci sayısı 1000 basamaklıdır. 

örnek: 12.   Fibonacci   sayısı   144   olduğundan   üç   basamaklı   ilk   Fibonacci   sayısı F12dir.

>Soru8.py

```
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

```


**Soru 9)** 10001’inci asal sayıyı bulunuz.

>Soru9.py

```
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
```

**Soru 10)** 2 milyondan daha küçük tüm asal sayıların toplamını bulunuz.

>Soru10.py

```
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
```



**Soru 11)** 100!’in rakamları toplamını bulunuz.

örnek: 10!= 3628800 olduğundan rakamları toplamı 27’dir

>Soru11.py

```
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
```



**Soru 12)** 1-20 arası tüm sayılara kalansız bölünebilen en küçük tam sayıyı bulunuz.

>Soru12.py

```
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
```


**Soru 13)** Aşağıdaki program ne çıktı verir?

>Soru13.txt

```
      x = 3 
      if 2 > x : 
        print 'First' 
      else : 
        print  'Second' 
        if 2 > x : 
          print 'Third' 
        print 'Fourth' 
      print `Fifth'
```
 Çıktı: 
```
Second
Fourth
Fifth`
```
**Soru 14)** Aşağıdaki program ne çıktı verir?

>Soru14.txt

```
      words = 'this IS NoT EvEN' 
      print words.title() 
      print words.replace("IS", 'was') 
      print words.upper() 
      print words * 2
```

 Çıktı: 
```
This Is Not Even
this was NoT EvEN
THIS IS NOT EVEN
this IS NoT EvENthis IS NoT EvEN
```
**Soru 15)** Aşağıdaki programdaki hatayı bulunuz. 

>Soru15.py

```
      line = raw_input("Type a word") 
      print "You typed", line 
      line = line + "h" 
      num = int(line) 
      print "You typed the number ", num  
```
Cevap: Dördüncü satırda hata verir.Çünkü string olan bir değişken integer'a dönüştürmeye çalışılıyor.


**Soru 16) ** Aşağıdaki algoritma ne iş yapmaktadır?

>Soru16.txt

```
      A1. Basla; 
      A2. a,b değerlerini oku; 
      A3. x=a, y=0; 
      A4. Eğer (x>=b) değilse A7'ye git; 
      A5. x=x-b; 
      A6. y=y+1; A4'e dön; 
      A7. x ve y’yi yazdır; 
      A8. Dur.
```
Cevap: Bu algoritma bölüm işlemi yapmaktadır. 'a' değişkenini ve 'b' değişkenini girdiğimizde bize bölüm ve kalanı vermektedir.


**Soru 17)** Aşağıda kuralları tanımlanmış oyunun algoritmasını yazınız.

```
      * Kullanıcıdan n sayısını okuyup 1’den n’e kadar sayılar sırayla yazılır.
      * İlk turda soldan sağa doğru önce ilk sayı, sonra birer atlayarak listenin sonuna kadar diğer sayılar çıkartılsın.İkinci turda ise  aynı işlem sağdan sola doğru tekrarlansın.
      * Son kalan sayı çıktı olarak verilmelidir.
      Örnek:
      Kullanıcıdan girdi olarak 9 okunursa oyun aşağıdaki gibi çalışmalıdır:
      1 2 3 4 5 6 7 8 9
      2 4 6 8
      2 6
      6
```


**Soru 18)** P(n); girdi olarak n alıp çıktı olarak n’den küçük veya eşit asal sayıların sayısını veren bir fonksiyon olsun. Örneğin P(1)=0, P(2)=1 ve P(100)=25 değerindedir. Bu fonksiyonun akış şemasını çiziniz

>Soru18.py

```
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

```

Kodun üzerinden akış şemasını çıkarabilirsiniz.

**Soru 19)** Yazacağınız python programında random modülünü kullanarak 1 ile 100 arasında rasgele sayılar üretilsin. Rasgele sayı üretmeyi, üretilen sayı 42 olana kadar tekrar edilsin ve kaçıncı tekrarda hedefe ulaşıldığını çıktı olarak versin.

>Soru19.py

```
import random

kontrol = True
sayac = 0

while kontrol:
    rastgele_sayi = random.randint(1,100)
    if rastgele_sayi == 42:
        kontrol=False
    sayac = sayac + 1

print sayac, " denemede hedefe ulasildi"


```


**Soru 20)** Yazacağınız python kodu kullanıcıdan n değerini okuyup n. Fibonacci sayısının basamak değerlerinin toplamını döndürmelidir. Örneğin girdi olarak 9 alınca onuncu Fibonacci sayısı olan 34’ün basamak değerlerini toplayıp 7 çıktısını vermelidir.

>Soru20.py


```
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


```



