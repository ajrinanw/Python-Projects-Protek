#PHYTON PROJECT 03

def bintang(n) :
    top = int(n/2 + 1)
    for i in range(1, n+1) :
        formasi = "*" * (1 + (i-1)*2)
        print(formasi.center(25))
        
        if(i == top) :
            for i in range(top - 1, 0, -1) :
                formasi = "*" * (1 + (i-1)*2)
                print(formasi.center(25))
                
            break


bintang(7)
bintang(13)
