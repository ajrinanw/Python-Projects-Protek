#PHYTON PROJECT 04

import random

def randomstring(x,n) :
    randomlist = []
    
    for i in range(n) :
        p = list(random.sample(x, len(x)))
        q = ''.join(p)
        
        if(q in randomlist) :
            continue
        else :
            randomlist.append(q)
            print(q)

            
kata = input("Masukkan kata yang ingin Anda acak : ")
jumlah = int(input("Masukkan jumlah hasil acakan yang Anda inginkan : "))

randomstring(kata,jumlah)
