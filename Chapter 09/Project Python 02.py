#PHYTON PROJECT 02

def bintang(n) :
    for i in range(1, n+1) :
        formasi = "*" * (1 + (i-1)*2)
        print(formasi.center(25))


bintang(4)
bintang(13)

