
#Data Manipulation

# NumPy (Numeric Phyton) Giriş:

# Listelere benzerdir ancak farkı; verimli veri saklaması  ve vektörel operasyonları gerçekleştirebilmesidir. 
# Listede saklanan 3 tane aynı tip eleman olduğunu düşünelim yani 3 tane int değer barındırıyorsa her biri için ayrı yer tutar. Ancak array'lerde kullanılacak veri tipleri arasında bir ayrım yoktur; sabitlenmiş (fix type) verilere zorladığı ve her biri için tek bir yer tuttuğundan daha verimlidir.

# Neden NumPy?

a=[1,2,3,4]
b=[2,3,4,5]

print(a)
print(b)

#Üç vektör çarpmak istersek, her seferinde bu işlemi yapmak karmaşıklık yaratacaktır

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
print(ab)

import numpy as np

array_a = np.array(a)
array_b = np.array(b)

print(array_a)
print(array_b)

print(array_a*array_b)

# NumPy Array'i Oluşturmak : Tek boyutlu array vektör, iki boyutlu array matristir.

import numpy as np
array1 = np.array([1,2,3,4,5])
print(array1)

type(array1)

#Fix type tuttuğu için her birini float formatta oluşturur.

np.array([3.14,4,2,13])

np.array([3.14,4,2,13],dtype="float32")

np.array([3.14,4,2,13],dtype="int")

# Sıfırdan Array Oluşturma 

zeros = np.zeros(10,dtype="int")
zeros

type(zeros)

ones = np.ones((3,5),dtype="int")
ones

#Belirli bir sayıdan oluşan array oluşturmak istersek;
#(np.full(satır,sütun),hangi sayı?)

np.full((3,5),7)

#Doğrusal bir dizi oluşturalım:0'dan 31'e kadar 3'er artan dizi (np.arange(start,stop,step))
#np.arange(start,stop,step)

np.arange(0,31,3)

#İki değer arasında belirli bir eleman sayısı için dizi oluşturma: 0 ile 1 arasında 10 sayı (np.linspace(start, stop, num=50, dtype="")
#np.linspace(start,stop,num of element,dtype = int)

np.linspace(0,20,10,dtype="int")

#Belirli bir dağılım yapısına uygun dizi oluşturalım: Standart sapma ya da ortalamaya göre (Ortalama 10, std sapma 4)
np.random.normal(10,4,(3,4))

#Integer değerlerden rastgele bir dizi oluşturursak: 0 ile 7 arasında 4 sayı türetelim

np.random.randint(0,7,4).reshape(2,2)

#Integer değerlerden rastgele bir matris oluşturursak: 0 ile 15 arasında 3X2 lik bir matris türetelim
#np.random.randint(start,stop,size/num of elem)

np.random.randint(0,15,(3,2))

# NumPy Array Özellikleri 

# ndim: Boyut sayısı:
# shape: Kaça kaçlık matris
# size: Toplam eleman sayısı (satır * sütun)
# dtype: array veri tipi


import numpy as np

# 0'dan 10'a kadar rastgele 10 değer:

a = np.random.randint(0,10,size=10)
a

print("Boyut:",a.ndim)
print("Satır&Sütun:",a.shape)
print("Eleman Sayısı:",a.size)
print("dtype:",a.dtype)

# İki boyutlu array için:

b= np.random.randint(0,10,size=(3,5))
b

print("Boyut:",b.ndim)
print("Satır&Sütun:",b.shape)
print("Eleman Sayısı:",b.size)
print("dtype:",b.dtype)

# NumPy Array'i Yeniden Şekillendirmek

import numpy as np
x= np.arange(1,10)
x

x.reshape(3,3)

# Elimizdei tek boyutlu vektörü bazen matrise çevirme ihtiyacımız olur:

print(x.ndim)
print(x.shape)

print(x)
print(x.reshape(1,9))

y= x.reshape(1,9)


print(x.ndim)
print(x.shape)

print(y.nd"im)
print(y.shape)

# Birleştirme (Concatenate)

x = np.array([1,2,3])
y = np.array([4,5,6])

#Yatay  birleştirme(axis = 1, default form):

x= x.reshape(1,3)
y = y.reshape(1,3)

print(x)
print(y)

np.concatenate([x,y],axis=1)

# Dikey  birleştirme(axis = 0):

x= x.reshape(1,3)
y = y.reshape(1,3)

print(x)
print(y)

np.concatenate([x,y],axis=0)

# 3.arrayi ekleyelim:

z=np.array([7,8,9])

print(np.concatenate([x,y,z]))

# 2 Boyutlu array'leri birleştirelim:

a= np.array([[1,2,3],
             [4,5,6]])
print(a)

# 0 satırları, 1 sütunları ifade eder;0 seçersek satırları birleştirir
np.concatenate([a,a],axis=0)

# 0 satırları, 1 sütunları ifade eder;1 seçersek sütunları birleştirir

np.concatenate([a,a],axis=1)

# Array Ayırma (Splitting) 

import numpy as np

x= np.array([1,2,3,99,99,3,2,1])
print(x)

np.split(x,[3,5])

#Kaçıncı index'lere kadar böleceksek [] ler içinde index'leri belirtiriz.
#parantez içindeki indexler dahil edilmez, bu indexlere kadar süpürerek ayırır.

np.split(x,[3,5,6])

#Böldüğümüz her bir array'i bir değişkene atayalım:

a,b,c,d  = np.split(x,[3,5,6])

print(a)
print(b)
print(c)
print(d)

# 2 Boyutlu Array Ayırma:

m = np.arange(0,16).reshape(4,4)
print(m)

# 2.satırdan sonraki kısmı bölüp yana ekleyelim:

ust,alt = np.vsplit(m, [2])
print("Üst:",ust)
print("Alt:",alt)

# 2.satırdan sonraki kısmı bölüp dikey ekleyelim:

sol,sag = np.hsplit(m, [2])
print("Sol:",sol)
print("Sağ:",sag)

# Array Sorting 

v = np.array([2,1,4,3,5])

np.sort(v)

print(v)

v.sort()

# v.sort() metodu inplace=True mantığı ile çalışır, yani mevcut array üzerinde değişiklik yapar, ancak np.sort(v) ile mevcut korunur.

print(v)

# 2 Boyutlu Array'de Sıralama:

m=np.random.normal(20,5,(3,3))
print(m)

# Satırları sıralayalım:

print(np.sort(m,axis=1))

# Sütunları sıralayalım:

print(np.sort(m,axis=0))

np.arange(0,10,3)

# Slicing ile Elemanlara Erişmek 

import numpy as np
a = np.arange(20,30,1)
print(a)

# İlk elemandan 23'e kadar getir:

a[0:3]

# Belirli bir index'ten sonuncuya kadar gitmek:

a[3:]

# 1.index'ten başla sonuncu elemana kadar 2'şer atlayarak ilerle:
a[1::2]
      
# 1.index'ten başla sonuncu elemana kadar 2'şer atlayarak ilerle:
a[2::2]

# İlk index'ten başla sonuncu elemana kadar 3'er ilerle:
a[0::3]
      
#2 Boyutlu Slice İşlemleri:

m =np.random.randint(10,size=(5,5))
print(m)

#Tüm satırları al, sütunlardan ilkini al

m[:,0]

# Tüm sütunları al,satırlardaın ilkini al

m[0,:]
m[0]

#Hem satır hem sütun seçelim, 2.satır ile tüm sütunları alalım:

m[1,:]

#İlk 2 satırı al, sütunlardan son iki sütun hariç al:

m[0:2,0:3]

#Tüm satırları, 0 ve 1.sütunu al:

m[:,0:2]

m

#2.ve 3.satır ile 1. ve 2.sütunu alalım:

m[1:3,0:2]

# Alt Küme Üzerinde İşlem Yapmak :Array'in alt kümesi üzerinde işlem yaptığımızda ana veri setimizde de değişiklik olacaktır. Bu değişikliğin ana veri setinde olmasını istemiyorsa alt kümenin bağımsızlaştırılması gerekir.

import numpy as np
a = np.random.randint(10,size=(5,5))
a

alt_a = a[0:3,0:2]
alt_a

#Alt kümede değişiklik yapalım:

alt_a[0,0] = 99999
alt_a[1,1] =888

print(alt_a)

#Çok büyük array'lerde değişiklik yapmak istediğimizde performans olarak bu değişikliği alt kümede yapmak tercih edilir. 
#Ancak ana kümede de değişiklik gerçekleşmesini istemiyorsak alt kümeyi "copy metodu" ile bağımsızlaştırmalıyız.

a = np.random.randint(10,size=(5,5))
a

a_copy = np.copy(a)
alt_a = a_copy[0:3,0:2]

alt_a[0,0] = 99999
alt_a[1,1] =888

print(alt_a)

print(a_copy)
print(a)

# Fancy Index ile Elemanlara Erişmek 

import numpy as np
v = np.arange(0,30,3)

print(v)

# 3 ve 5 nolu indexlerine erişelim:

v[3]

v[5]

#1. 3. ve 5.index'leri bir arada görmek istersek:

[v[1],v[3],v[5]]

#Basit bir vektör için erişebildik, ancak çok büyük bir array'den yakalamak istersek:

for i in range(0,len(v)):
    print(v[i])

al_getir = [1,3,5]

#Fancy Index ile 1,3,5. index'i seçmek istersek, bir liste oluşturur "in" mantığı ile içinde aratırız: v[list1]

v[al_getir]

#2 Boyutta Fancy Uygulaması:

m = np.arange(9).reshape(3,3)
print(m)

satir = np.array([0,1])
sütun = np.array([0,2])

print(satir)
print(sütun)

print(m[satir,sütun])

#Basit Index ile Fancy Index:

m[0,[]]

#Slice ile Fancy Index:
 
m[0:,[1,2]]

# Koşullu Eleman İşlemleri

import numpy as np
v = np.array([1,2,3,4,5])
print(v)

#Karşılaştırma operatörleri ile işlemleri gerçekleştirelim:

#5'ten büyük değer var mı?
v>5

#5'ten büyük değerleri getir:
v[v>5]

#3'ten büyük değer var mı?
v>3

#3'ten büyük değerleri getir:
v[v>3]

#3 ve 3'ten küçük elemanları getirelim:
v[v<=3]

#3 varsa getir:
v[v==3]

#2'ye eşit olmayanları getir:
v[v!=2]

# Matematiksel İşlemler

import numpy as np
v = np.array([1,2,3,4,5])
print(v)

v - 1
v**2
v*5
v/4

      
# ufunc: 
    
print(v-1)
print(np.subtract(v,1))

print(v+7)
print(np.add(v,7))

print(v*5)
print(np.multiply(v,5))

print(v/4)
print(np.divide(v,4))

print(v**2)
print(np.power(v,2))

print(v**3)
print(np.power(v,3))

#2'ye bölümden kalanlar:

print(v % 2)
print(np.mod(v, 2))

#Mutlak değer:

m = np.array([-1,-5,2,-17,9])

print(m)
print(np.absolute(m))

      
#Trigonometrik Fonksiyonlar:
np.sin(360)
np.cos(180)

#Logaritmik İşlemler:
np.log(v)

#Logaritmik fonksiyonun derecesini ayarlamak istersek:
np.log10(v)
np.log2(v)

#NumPy'da kullanılan fonksiyonlar neler?
?np

# İstatistiksel Hesaplamalar

import numpy as np
v = np.array([1,2,3])
print(v)

np.mean(v)

np.min(v)

np.max(v)

np.sum(v)

np.std(v)

# Numpy ile İki Bilinmeyenli Denklem Çözümü

import numpy as np

5*Xo +X1 =12 
Xo+3*X1 =10

#Yukarıdaki denklemi array'e dönüştürelim:

a = np.array([[5,1],[1,3]])
b = np.array([12,10])

print(a)
print(b)

x = np.linalg.solve(a,b)

print(x)

Xo              X1
[1.85714286 2.71428571]
