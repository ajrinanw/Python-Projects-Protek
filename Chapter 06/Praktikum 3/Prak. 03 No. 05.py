#CHAP.06 PRAK.03 NOMOR 05

from operation import*

#***Nomor 5a***
a=2
b=4
c=6

x= kali (b,c)
y= jumlah (a,x)
z= kurang (y,b)
print (a, "+", b, "*", c, "–", b, "=", z)

#ATAU

x= kali(4,6)
y= jumlah(2,x)
z= kurang(y,4)
print (z)

#***Nomor 5b***
a=4
b=7
c=6
d=9

m= jumlah (a,b)
n= kurang (c,d)
o= kali (m,n)
print ("(",a, "+",b,")", "*", "(",c, "-",d,")", "=", o)

#ATAU

m= jumlah (4,7)
n= kurang (6,9)
o= kali (m,n)
print (o)

#***Nomor 5c***
a=10
b=2
c=7
d=5
e=12
f=34

p= jumlah(a,b)
q= jumlah(c,d)
r= kurang(e,f)
s= bagi(p,q)
t= bagi(s,r)
print ("(",a, "+",b,")", "/", "(",c, "+",d,")", "/", "(",e, "-",f,")", "=", t)

#ATAU

p= jumlah(10,2)
q= jumlah(7,5)
r= kurang(12,34)
s= bagi(p,q)
t= bagi(s,r)
print (t)
