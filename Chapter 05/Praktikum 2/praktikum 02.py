#CHAPTER 05 PRAKTIKUM 02
#***nomor 2***
i = 0
while (i < 10):
    print ("Hello World")
    i += 1

#***nomor 5***
i = 2
while (i <= 20):
    print ("Hello World")
    i += 2

#***nomor 6***
i = 0
while True:
    print ("Hello World")
    i += 1
    if (i == 10):
        break

#***nomor 8***
#kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1

#***nomor 10***
kolom = 0
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j <= kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1
    kolom += 1

#***nomor 11***
from random import randint
while True:
    bil = randint(0,10)
    print (bil)
    if bil == 5:
        break

#***nomor 13***
from random import randint

i = 0
while True:
    bil = randint(0,10)
    print (bil)
    i = i+1
    if bil == 5:
        break

print ("Jumlah Perulangan : ", str(i))



