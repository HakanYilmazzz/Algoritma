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
