#CHAP.06 PRAK.O4 LATIHAN 04

def sum(*n):
    i=0
    for x in n:
        i+=x
    print(i)


def average(*n):
    i=0
    j=0
    for x in n:
        i+=x
        j+=1
    average=i/j
    print(average)


def maks(*n):
    maks=n[0]
    for i in (n):
        if(i>maks):
            maks=i
    print(maks)


def min(*n):
    min=n[0]
    for i in (n):
        if(i<min):
            min=i
    print(min)

    

    
