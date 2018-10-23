# TEMEL BILGILER

**1** –> Türkçe karakter sorununu duzeltiyor: coding: cp1254

**2**--> Butun matematiksel islemleri tamsayı olarak alacak

    from future import division

**3** --> printf ve degisken ornegi
```
a = 5
b = 3
print "a'yi b'ye bolersek", a / b, "elde ederiz"
print a, "sayısı", b, "sayısından büyüktür"
print "%s ile %s çarpılırsa %s elde edilir" %(a, b, a*b)
```

**4** --> raw_input fonksiyonu (string = karakter)
```
parola = raw_input("Lütfen parolanızı girin:")
print "Hosgeldiniz!"
print "Girdiğiniz parola: ", parola
```
**5**--> input fonksiyonu (integer = sayi)
```
a = input("Lütfen bir sayı girin:")
print a
```
**NOT** : raw_input() ile input() arasindaki fark
```
//input()
a = input("Lütfen bir sayı girin:")
b = input("Lütfen başka bir sayı daha girin:")
print a + b 
a=5
b=42 olsun 
sonuc = 47 olur

//raw_input()
a = raw_input("Lütfen bir sayı girin:")
b = raw_input("Lütfen başka bir sayı daha girin:")
print a + b 
a=5 
b=42 olsun
 sonuc = 542 olur
```
**6** --> \n bir asagidaki satira iner :  ``` print "Birinci satır\nİkinci satır\nÜçüncü satır" ```

**7** --> \t 4 karakter bosluk saglar: ```print "uzak... \tçok uzak"```

**8**--> Dönüştürme İşlemleri
```
    karakteri sayiya donusturme

     a = "23"
      int(a)  
```
    ekran cıktısı 23 olur
```
    sayiyi karaktere donusturme
```
    a = 23
    str(a) 
```
ekran cıktısı ‘23’ olur
```
**KOSULA BAGLI DURUMLAR** --> if / else / elif
```
parola = "python"
cevap = raw_input("Lütfen parolanızı giriniz: ")
if cevap == parola:
    print "Parola onaylandı! Programa hoş geldiniz!"
elif cevap=="PYTHON":
    print "Parola onaylandı! Programa hoş geldiniz!"
else:
    print "Ne yazık ki, yanlış parola girdiniz!"
```
#### GENEL ORNEK:

-- coding: utf-8 --
```
    secenek1 = "(1) toplama"
    secenek2 = "(2) çıkarma"
    secenek3 = "(3) çarpma"
    secenek4 = "(4) bölme"
    
    print secenek1
    print secenek2
    print secenek3
    print secenek4

soru = raw_input("Yapılacak işlemin numarasını girin: ")

if soru == "1":
     sayi1 = input("Toplama için ilk sayıyı girin: ")
     print sayi1
     sayi2 = input("Toplama için ikinci sayıyı girin: ")
     print sayi1, "+", sayi2, ":", sayi1 + sayi2
if soru == "2":
     sayi3 = input("Çıkarma için ilk sayıyı girin: ")
     print sayi3
     sayi4 = input("Çıkarma için ikinci sayıyı girin: ")
     print sayi3, "-", sayi4, ":", sayi3 - sayi4
if soru == "3":
     sayi5 = input("Çarpma için ilk sayıyı girin: ")
     print sayi5
     sayi6 = input("Çarpma için ikinci sayıyı girin: ")
     print sayi5, "x", sayi6, ":", sayi5 * sayi6
if soru == "4":
     sayi7 = input("Bölme için ilk sayıyı girin: ")
     print sayi7
     sayi8 = input("Bölme için ikinci sayıyı girin: ")
     print sayi7, "/", sayi8, ":", sayi7 / sayi8
```

[============================================================================]

### DONGULER

**1** --> `while` Dongusu
```
a = 0
while a < 100:
    a = a + 1
    print a
```
**2** --> `for` Dongusu
```
for i in range(1, 100):
     print i
```
**3** --> `range()` fonksiyonu (Bu fonksiyon Pythonda sayı aralıklarını belirtmemizi sağlar.)
```
print range(1, 100, 2)
```
sonuc = 1 ile 100 arasındaki sayilari ikişer ikişer yazdıracak [1,3,5,…,99]


**4** -->` len()` fonksiyonu (Bu fonksiyon, karakter dizilerinin uzunluğunu gösterir.)
```
a = "Afyonkarahisar"
print len(a)
```
**5** --> `break` deyimi (bir döngüyü sona erdirmek gerektiği zaman kullanılır.)
```
    kullanici_adi = "kullanici"
    parola = "parola"

while True:
     soru1 = raw_input("Kullanıcı adı: ")
     soru2 = raw_input("Parola: ")

     if soru1 == kullanici_adi and soru2 == parola:
        print "Kullanıcı adı ve parolanız onaylandı."
        break
     else:
        print "Kullanıcı adınız veya parolanız yanlış."
        print "Lütfen tekrar deneyiniz!"
```
**6** --> `continue` deyimi (Bu deyim ise döngü içinde kendisinden sonra gelen her şeyin es geçilip döngünün en başına dönülmesini sağlar.)
```
while True:
     s = raw_input("Bir sayı girin: ")
     if s == "iptal":
        break
     if len(s) <= 3:
        continue
     print "En fazla üç haneli bir sayı girin."
```

[============================================================================]

 ### LISTELER (list)
```
liste = ["Hale", "Jale", "Lale", 12, 23]
len(liste)
```
**1** --> `append()` (Listeye yeni bir öğe eklemek için metodundan faydalanıyoruz)
```
liste.append("Mehmet")
```
append() fonksiyonu yalnız bir eleman ekler ve en sona ekler??
```
   liste[0]
```
  listenin belli bir elemanına ulaşmak için bu terim kullanılır.

**2** --> `insert()` (Listenin herhangi bir noktasına öğe ekleyebiliyoruz.)
```
    liste.insert(1, "Ahmet")
```

Bu metot da tıpkı append() metodunda olduğu gibi listeye yalnızca bir adet öğe eklememize izin verir.

**3**--> `extend()` (oluşturduğumuz listeleri “genişletmemizi” sağlar.)
```
yeni_liste = ["Simovic", "Prekazi", "Jardel", "Nouma"]
liste.extend(yeni_liste)
liste = liste + yeni_liste
```
iki kodunda görevi listeleri birleştirmek ve her zaman listenin sonuna ekler.

 **4** --> `remove()` (listemizden isim vererek öğe çıkarmak.)
```
     liste.remove("Nouma")
```
veya

**5** --> `pop()` (listeler ile birlikte kullandığımız pop() metodu ise listeden bir öğe silerken, bu sildiğimiz öğenin ekrana yazdırılmasını sağlıyor.)

(listemizden sayi vererek öğe çıkarmak.)
```
liste.pop()
```
veya
```
liste.pop(0)
```
**6** -->` index()` (Bu komut, öğenin liste içinde kaçıncı sırada olduğunu gösterir.)
```
print liste.index("Jardel")
```
**7** -->` sort()` (listemizdeki öğeleri alfabe sırasına dizmeye yarar.)
```
liste.sort()
```
**8** -->` reverse()` (Bu metot listedeki öğelerin sırasını ters cevirir.)
```
liste.reverse()
```
**9** --> `count() ` (Bu metot liste içinde bir öğenin kaç kez geçtiğini söyler.)
```
liste.count("Prekazi")
```

  Nasıl liste oluşturacağımızı --> **liste = []**

   bu listeye nasıl yeni öğeler ekleyeceğimizi --> **liste.append(), liste.insert()**

   listemizi nasıl genişleteceğimizi -->** liste.extend()**

   eklediğimiz öğeleri nasıl çıkaracağımızı --> **liste.remove(), liste.pop()**

   liste içindeki öğelerin sırasını bulmayı -->**liste.index()**
   
   öğeleri abc sırasına dizmeyi -->**liste.sort()**
   
   öğelerin sırasını ters çevirmeyi (cba) -->**liste.reverse()**
   
   listedeki öğelerin liste içinde kaç kez geçtiğini bulmayı -->**liste.count()**
   
   **liste[-1]** = listedeki son öğeyi çağırmak istersek
   
   **liste[2:4]** = listedeki 2. ve 3. öğeleri yazdıracaktır.
   
   **liste[5:5] = [“domates”, “salata”]** listenin en sonuna bir veya birden fazla öğe ekle
   
   **liste[3:3] = ["kebap", "lahmacun"]** listenin 3.sırasına bir veya birden fazla öğe ekle
   
   **liste[2:3] = []** listenin 2. sırasındaki öğeyi silme
   
   **liste[2:3] = ["nane", "limon"]** listenin 2.sırasındaki öğeyi silip yerine bir veya b’fazla öğe ekle
   
   **liste[2] = ["ruj", "maskara", "rimel"]** listenin 2. sırasındaki öğeyi silip yerine bir veya birden fazla öğeye sahip bir liste yerleştirmek


[============================================================================]

### DEMETLER (tuple)

   Demetler listelere benzer. Ama listeler ile aralarında çok temel bir fark vardır
    Listeler üzerinde oynamalar yapabiliriz. Yani öğe ekleyebilir, öğe çıkarabiliriz. Demetlerde ise böyle bir şey yoktur.
```
    demet = “Ali”, “Veli”, 49, 50 veya demet2 = (“Ali”, “Veli”, 49, 50) aynı şey
    demet = () boş bir demet
    demet = (“su”,) tek öğeli bir demet
```

[============================================================================]


### SOZLUKLER (ordereddict)

```
telefon_defteri = {"Ahmet": "0533123 45 67","Salih": "0532321 54 76","Selin": "0533333 33 33"}
```
**1** --> yeni öğe ekleme
```
telefon_defteri["Zekiye"] = "0544 444 01 00"
```
**2**--> sözlüğümüzdeki bir öğenin değerini değiştirmek
```
telefon_defteri["Salih"] = "0555 555 55 55"
```
**3** --> bir öğeyi listeden silmek istersek
```
del telefon_defteri["Salih"]
```
**4** --> sözlükteki bütün öğeleri silmek istersek
```
telefon_defteri.clear()
```
**5** --> `keys()` metodu bir sözlükteki anahtarları,
```
print telefon_defteri.keys() #['Ahmet', 'Salih', 'Selin']
```
**6** `values()` metodu ise sözlükteki değerleri verir.
```
print telefon_defteri.values() #['0533 123 4567','0532 321 5476','0533 333 3333']
```
#### SOZLUKLER İLE İLGİLİ BİR ORNEK 
```
soru = raw_input("Şehrinizin adını tamamı küçük harf olacak şekilde yazınız: ")
cevap = {"ankara":"açık ve güneşli", "izmir":"bulutlu"}
print cevap.get(soru,"Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır.")
```

`get()` fonksiyonu bize sözlük içinde bir değerin varolup olmadığını denetleme imkânının yanısıra, adı geçen değerin sözlük içinde varolmaması durumunda kullanıcıya gösterilecek bir mesaj seçme olanağı da sunar.
if deyimleri yerine sözlüklerden yararlanmanın faydaları

**1** – > Öncelikle sözü geçen senaryo için sözlükleri kullanmak programcıya daha az kodla daha çok iş yapma olanağı sağlar.

**2**  – > Sözlük programcının elle oluşturacağı “if-elif-else” bloklarından daha performanslıdır ve bize çok hızlı bir şekilde veri sorgulama imkânı sağlar.

**3** – > Kodların daha az yer kaplaması sayesinde programın bakımı da kolaylaşacaktır.

**4** – >Tek tek “if-elif-else” blokları içinde şehir adı ve buna ilişkin hava durumu bilgileri tanımlamaya kıyasla sözlük içinde yeni “anahtar-değer” çiftleri oluşturmak daha pratiktir.

#### SIRALI SOZLUKLER
```
from collections import OrderedDict
personel = OrderedDict([("Ahmet", "19.01.2013"),
... ("Mehmet", "21.03.2013"), ("Selin", "30.06.2013")])
```
yada
```
personel = OrderedDict()
personel["Ahmet"] = "19.01.2013"
personel["Mehmet"] = "21.03.2013"
personel["Selin"] = "30.06.2013"
print personel
```
**ekran cıktısı** =``` OrderedDict([('Ahmet', '19.01.2013'), ('Mehmet', '21.03.2013'),(‘Selin’, ‘30.06.2013’)])```
`personel.keys()` **ekran cıktısı** =` ['Ahmet', 'Mehmet', 'Selin']`
`personel.values()` **ekran cıktısı** = `['19.01.2013', '21.03.2013', '30.06.2013']`
`print personel.get("Sedat", "Böyle biri yok!") `**ekran cıktısı **= `Böyle biri yok!`


[============================================================================]

### FONKSIYONLAR

**1** --> Fonksiyonu Tanımlamak
```
def fonksiyon_adi():
    print "merhaba dünya!"
```
`fonksiyon_adi()` Fonksiyonu cagıran kod

**2** --> Fonksiyonlarda Parametre Kullanımı
```
def selamla(isim):
    print "merhaba, benim adım %s!" %isim
selamla("Ahmet Efendi")
```
ekran cıktısı = `merhaba, benim adım Ahmet Efendi!` olur.
```
def carp(liste):
     a = 1
     for i in liste:
        a = a * i
     print(a)
sayilar = [3, 5, 7]
carp(sayilar)
```
ekran cıktısı = `105`

**3** --> İsimli Argümanlar
```
def kayit_ekle(isim, soyisim, sehir, meslek, tel, adres):
     kayit = {}
     kayit["%s %s" %(isim, soyisim)] = [sehir, meslek, tel, adres]
     print "\nBağlantı bilgileri kayıtlara eklendi!\n"
     for k, v in kayit.items():
         print k
         print "-"*len(k)
         for i in v:
             print i
isi = raw_input("isim: ")
soy = raw_input("soyisim: ")
seh = raw_input("şehir: ")
mes = raw_input("meslek: ")
tel = raw_input("telefon: ")
adr = raw_input("adres: ")
kayit_ekle(isi, soy, seh, mes, tel, adr)
```
**4** --> Gömülü Fonksiyonlar

http://docs.python.org/library/functions.html

**5**–> `global` Deyimi
```
def fonk():
     global a
     a = 5
     print a
fonk()
print "a'nın değeri: ", a
```
ekran cıktısı =` a'nın değeri: 5`

**6** --> `return` Deyimi
```
def sayi_isle():
     sor = input("bir sayı girin: ")
     return sor
sayi = sayi_isle()
print "girdiğiniz sayı: %s" %sayi
if sayi % 2 == 0:
    print "girdiğiniz sayı çifttir"
else:
    print "girdiğiniz sayı tektir"
print "girdiğiniz sayının karesi: %s" %sayi ** 2
print "girdiğiniz sayının küpü: %s" %sayi ** 3
```
**7** --> `pass` Deyimi (bu deyim herhangi bir işlem yapmadan geçeceğimiz durumlarda kullanılır.)
```
def deneme():
     liste = []
     while True:
         a = raw_input("Giriniz: ")
         if a == "0":
             pass
         else:
            liste.append(a)
            print liste
deneme()
```
**8**  – >` try… / except…` (Python’da hata yakalamak için kullanılır.)
```
	try:
	   ilk = int(raw_input("Bölme işlemi için ilk sayıyı girin: "))
	    	    ikinci = int(raw_input("Şimdi de ikinci sayıyı girin: "))
	    	    sonuc = float(ilk) / ikinci
	    	    print sonuc
	    	except ZeroDivisionError:
	    	    print "Lütfen sayıyı 0'a bölmeye çalışmayın!"
	    	except ValueError:
	    	    print "Lütfen harf değil, sayı girin!"
```
**9** – > `count` metodu (bir karakter dizisi içinde bir karakterden kaç adet bulunduğunu denetleme imkânı verir.)
```
    besiktas = "Sinan Paşa Pasajı"
    besiktas.count("a")
```
ekran cıktısı = `5`

**10** – > `find` metodu (bir karakterin, karakter dizisi içinde hangi konumda yer aldığını söyler.)
```
    a = "armut"
    print a.find("a")
```
ekran cıktısı = `0`

**11** – >` a.upper() `karakterleri büyütür
```
print a.upper()
```
**12** – > `a.lower()` karakterleri kücültür
```
print a.lower()
```
**13** – >` a.isupper()` karakterlerin hepsi büyükse True degilse False yazar
```
print a.isupper()
```
**14** – > `a.islower() `karakterlerin hepsi kücükse True degilse False yazar
```
print a.islower()
```
**15** – > `a.capitalize()` baş harfi buyuk yazar
```
print a.capitalize()
```
**16** – > `a.replace(‘a’,‘b’)` aharfi yerine b harfi yazar
```
print a.replace('a','b')
```

**17** – >` import math`

 **18** – >` dir(math)`

 **19** – > `math.pi`

 **20** – >` math.e`

 **21**– > `math.factorial(5)`

 **22** – >` pow(2,3)`

[============================================================================]


### Örnekler

 1** Fibonacci**
```
f1,f2=1,1
n=input("kacinci sayiyi ogrenmek istiyorsunuz: ")
for i in range (3,n+1):
    fib=f1+f2
    f1,f2=f2,fib
print fib
```
#### 2  Asal sayi
```
number=input("sinir degeri girin: ")
for num in range(10,number):
    for i in range(2,num/2):
        if num%i==0:
            break
    else:
        print num
```
#### 3  Belli aralığı yazdırma
```
i=0
while i<7:
    print i 
    i=i+1
```
#### 4  try/except
```
a=raw_input("bir sayi girin: ")
try:
    print(int(a)/2)
except:
    print("sayi girmediniz")
```


> **Sonuna kadar geldiniz ,Tebrikler**  (&#x1F499;) 
