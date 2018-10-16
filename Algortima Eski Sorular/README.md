Algoritma_Eski_Sorular_ve_Çözümleri
==================================
<h4>Çanakkale On Sekiz Mart Üniversitesi Bilgisayar Mühendisliği</h4>
<h5>Algoritma ve Programlama Dersi<h5> 
Necdet hocanın önceki yıllarda sorduğu soruları ve çözümlerini içeren bir döküman

SORU 1) 2^1000 ’nin basamak değerleri toplamını bulan bir python kodu yazınız. 

İpucu:   Örneğin   2^15 ’in   değeri   32768   olduğundan   soru   1000   yerine   15   için   sorulsaydı  
cevap 3 + 2 + 7 + 6 + 8 = 26 olurdu. 

Soru 2) Eğer bir sayı kadar nokta kullanılarak bir üçgen oluşturulabiliyorsa o sayıya 
üçgen sayı denmektedir. İlk altı üçgen sayı (1,3,6,10,15,21) aşağıda gösterilmektedir. Buna 
göre kullanıcıdan okuduğu sayının bir üçgen sayı olup olmadığını belirleyen bir python 
programı yazınız. 
<img src="http://i.hizliresim.com/12yzzp.png" height="300"width="300"/>

Soru 3) 10 elemanlı ve elamanları tekrar edebilen biri dizinin elemanlarını 
tekrarsız bir şekilde sıralayan algoritmayı yazınız. İstediğiniz sıralama algoritmasını 
kullanabilirsiniz. 
      Örnek: {3,42,1,3,17,1,1,1,10,2} -> {1,2,3,10,17,42} 
      
Soru 4) Sadece çift Fibonacci sayılarını toplayarak 1000'i geçmeye çalışıyorsunuz. En son kaçıncı 
Fibonacci sayısı bu diziye dahil olacaktır?

Soru 5) a < b < c  olmak üzere  a^2 + b^2 = c^2  olan tam sayılara Pisagor üçlüsü denir.  a + b + c = 1 000
olacak şekilde tek bir Pisagor üçlüsü vardır. Onu bulmanız istenmektedir. 

Soru 6) Elinizde 1, 2, 5, 10, 25 ve 50 kuruşluk madeni paralarınız olsun. Bu paraları kullanarak 
toplamda 1 TL olusturmanız istenmektedir. Her seferinde her madeni para türünden mutlaka 
kullanmanız gerekmiyorsa kaç farklı şekilde 1 TL elde edilebildiğini hesaplayınız.

Soru 7) NxN’lik bir kare üzerinde en fazla kaç kare bulunduğunu hesaplayan programın 
akış şemasını çiziniz. (Örneğin 2x2’lik bir kare üzerinde 5 kare bulunabilir) 

Soru 8) Kaçıncı Fibonacci sayısı 1000 basamaklıdır. 
 
      örnek: 12.   Fibonacci   sayısı   144   olduğundan   üç   basamaklı   ilk   Fibonacci   sayısı  
F12dir.

Soru 9) 10001’inci asal sayıyı bulunuz. 

Soru 10) 2 milyondan daha küçük tüm asal sayıların toplamını bulunuz. 

Soru 11) 100!’in rakamları toplamını bulunuz.  
      
      örnek: 10!= 3628800 olduğundan rakamları toplamı 27’dir. 
      
Soru 12) 1-20 arası tüm sayılara kalansız bölünebilen en küçük tam sayıyı bulunuz. 

Soru 13) Aşağıdaki program ne çıktı verir? 

      x = 3 
      if 2 > x : 
        print 'First' 
      else : 
        print  'Second' 
        if 2 > x : 
          print 'Third' 
        print 'Fourth' 
      print `Fifth'
      
Soru 14) Aşağıdaki program ne çıktı verir?

      words = 'this IS NoT EvEN' 
      print words.title() 
      print words.replace("IS", 'was') 
      print words.upper() 
      print words * 2  
      
Soru 15) Aşağıdaki programdaki hatayı bulunuz. 

      line = raw_input("Type a word") 
      print "You typed", line 
      line = line + "h" 
      num = int(line) 
      print "You typed the number ", num  
      
Soru 16) Aşağıdaki algoritma ne iş yapmaktadır? 

      A1. Basla; 
      A2. a,b değerlerini oku; 
      A3. x=a, y=0; 
      A4. Eğer (x>=b) değilse A7'ye git; 
      A5. x=x-b; 
      A6. y=y+1; A4'e dön; 
      A7. x ve y’yi yazdır; 
      A8. Dur. 
Soru 17) Aşağıda kuralları tanımlanmış oyunun algoritmasını yazınız.<br/>
      * Kullanıcıdan n sayısını okuyup 1’den n’e kadar sayılar sırayla yazılır.<br/>
      * İlk turda soldan sağa doğru önce ilk sayı, sonra birer atlayarak listenin sonuna kadar diğer sayılar çıkartılsın.            İkinci turda ise aynı işlem sağdan sola doğru tekrarlansın.<br/>
      * Son kalan sayı çıktı olarak verilmelidir.<br/>
      Örnek:<br/>
      Kullanıcıdan girdi olarak 9 okunursa oyun aşağıdaki gibi çalışmalıdır:<br/>
      1 2 3 4 5 6 7 8 9<br/>
      2 4 6 8<br/>
      2 6<br/>
      6<br/>

Soru 18) P(n); girdi olarak n alıp çıktı olarak n’den küçük veya eşit asal sayıların sayısını veren bir fonksiyon olsun. Örneğin P(1)=0, P(2)=1 ve P(100)=25 değerindedir. Bu fonksiyonun akış şemasını çiziniz

Soru 19) Yazacağınız python programında random modülünü kullanarak 1 ile 100 arasında rasgele sayılar üretilsin. Rasgele sayı üretmeyi, üretilen sayı 42 olana kadar tekrar edilsin ve kaçıncı tekrarda hedefe ulaşıldığını çıktı olarak versin.

Soru 20) Yazacağınız python kodu kullanıcıdan n değerini okuyup n. Fibonacci sayısının basamak değerlerinin toplamını döndürmelidir. Örneğin girdi olarak 9 alınca onuncu Fibonacci sayısı olan 34’ün basamak değerlerini toplayıp 7 çıktısını vermelidir.
