#CHAP. 07 PRAK. 03 LATIHAN 02
try :

    namafile = input('Masukkan Nama File : ')
    file = open(namafile, 'a')

    lanjut = True
    while(lanjut==True):
        data = input('Masukkan Data yang Mau Ditambahkan : ')
        file.write(' ' + data)

        opsi = input('Mau Lagi ? (y/n) : ')
        if (opsi=='y'):
            lanjut = True
        elif (opsi=='n'):
            lanjut = False
        else :
            print('Input Tidak valid')
            break
    file.close()

except FileNotFoundError :
    print('File Tidak Ditemukan')
