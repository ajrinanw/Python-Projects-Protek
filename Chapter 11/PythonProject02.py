#PHYTON PROJECT 02

import os
from datetime import *

if(os.path.exists) :
        mode = 'a'

else :
        mode = 'w'

file = open('DataPeminjaman.txt', mode)

while True :  
    kode = input("\nMasukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    buku = input("Masukkan Judul Buku  : ")

    pinjam = date.today()
    kembali = pinjam + timedelta(days = 7)

    file.write(kode + '|' + nama + '|' + buku + '|' + str(pinjam) + '|' + str(kembali) + '\n')

    ulang = input("\nUlangi lagi (y/n)    : ")
    if (ulang == 'Y' or ulang == 'y') : 
        continue

    elif (ulang == 'N' or ulang == 'n') : 
        break

    else :
        print("Input Ivalid")
        break

file.close()
