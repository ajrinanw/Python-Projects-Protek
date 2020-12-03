#CAHPTER 08 LATIHAN
#***nomor 1***
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print(a)
print(b)

print( )
#***nomor 2***
a.insert(3,10)
b.insert (2,15)
print(a)
print(b)

print( )
#***nomor 3***
a.append(4)
b.append(8)
print(a)
print(b)

print( )
#***nomor 4***
a.sort()
b.sort()
print(a)
print(b)

print( )
#***nomor 5***
c=a[0:8]
d=b[2:10]
print(c)
print(d)

print( )
#***nomor 6***
e=[]
for i in range(len(c)):
    element=c[i] + d[i]
    e.append(element)    
print(e)

print()
#***nomor 7***
eTuple=tuple(e)

#***nomor 8***
minE=min(eTuple)
maxE=max(eTuple)
sumE=sum(eTuple)
print(minE)
print(maxE)
print(sumE)

print( )
#***nomor 9***
myString="python adalah bahasa pemrograman yang menyenangkan"

#***nomor 10***
huruf=set(myString)
print(myString)

print( )
#***nomor 11***
listHuruf=list(huruf)
listHuruf.sort()
print(listHuruf)
