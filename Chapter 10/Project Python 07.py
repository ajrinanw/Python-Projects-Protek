#PHYTON PROJECT 07

def enkripsi(teks, n) :
    dataTeks = list(teks)

    for i in range(len(dataTeks)) :
        if(dataTeks[i] != ' ') :
            teks = ord(dataTeks[i])
            acak = teks - n
            dataTeks[i] = chr(acak)

        else :
            continue

    hasil = ''.join(dataTeks)
    return hasil

try : 
    teks = input ("Masukkan teks hasil enkripsi     : ")
    n = int(input("Masukkan jumlah geseran enkripsi : "))
    hasil = enkripsi(teks, n)
    
    print("Teks asli dari {0} adalah : {1}".format(teks, hasil))

except ValueError :
    print("Inputan invalid")
