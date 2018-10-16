Bu algoritma bölüm işlemi yapmaktadır. 'a' değişkenini ve 'b' değişkenini girdiğimizde bize bölüm ve kalanı vermektedir.
Ben bu algoritmanın kodunu yazdım.Şöyleki;

a = input("a degerini girin: ")
b = input("b degerini girin: ")

x = a
y = 0

while True 
  if x<b :
    print x,y
    break
  else :
    x = x - b
    y = y + 1

Burada a ya 8 b ye 5 değerlerini verdiğimizde bize çıktı olarak x e 3 y ye 1 değerlerini verecek. 
