#CHAP.06 PRAK.O4 LATIHAN 03

def faktorial(n):
    faktorialN=1
    while(n>0):
        faktorialN=faktorialN*n
        n-=1
    return faktorialN

def kombinasi(a,b):
    c=a-b
    hasil=faktorial(a)/(faktorial(b)*faktorial(c))
    print(hasil)

def permutasi(a,b):
    c=a-b
    hasil=faktorial(a)/faktorial(c)
    print(hasil)

#***Nomor 3a***
a=5
b=3
kombinasi(a,b)

#***Nomor 3b***
a=10
b=7
permutasi(a,b)

