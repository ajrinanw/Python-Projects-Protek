#PHYTON PROJECT 03

from datetime import *

'''
#function tanpa menulis ulang (dengan pemanggilan)
import PythonProject01
'''

#function menulis ulang (manual)
def diffDate(x) :
    tanggal = x.split("-")
    dateList = []

    for i in tanggal :
        dateList.append(int(i))

    past = date(dateList[0], dateList[1], dateList[2])
    now = datetime.date(datetime.now())

    hasil = past - now
    result = (hasil.days)

    return result

file = open('DataPeminjaman.txt', 'r')

line = file.readlines()
kode = input("Masukkan Kode Member : ")

dataMember = {}
try :
    for i in range(len(line)) :
        if(kode in line[i]) :
            a = line[i].replace('\n', '')
            b = a.split('|')

            dataMember[kode] = [b[1], b[2], b[3], b[4]]

    print("\nData Peminjaman Buku")
    print("Kode Member              :", kode)
    print("Nama Member              :", dataMember[kode][0])
    print("Judul Buku               :", dataMember[kode][1])
    print("Tanggal Mulai Peminjaman :", dataMember[kode][2])
    print("Tanggal Maks Peminjaman  :", dataMember[kode][3])
    
    balik = print("Tanggal Pengembalian     :", datetime.date(datetime.now()))

    '''
    #penggunaan functin yang menggunakan impor
    telat = PythonProject01.diffDate(dataMember[kode][3])
    '''
    #penggunaan functin yang tulis ulang
    telat = diffDate(dataMember[kode][3])
    denda = 2000* abs(telat)

    if (telat >= 0) :
        print ("Terlambat                : 0 hari")
        print ("Denda                    : Rp. 0")
        

    else :
        print ("Terlambat                :", abs(telat), "hari")
        print ("Denda                    : Rp.", denda)

except KeyError:
    print ("Data Tidak Ditemukan")


