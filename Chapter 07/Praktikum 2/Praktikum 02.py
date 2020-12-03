#CHAPTER 07 PRAKTIKUM 02

try :
    #membuka dan mau membaca file
    file = open('C:/Users/asus/Documents/Python Projects/Python-Projects-Protek/Chapter 07/Praktikum 2/data.txt','r')

    #baca baris pertama dari file
    #simpan ke dalam variabel bil1 sebagai integer
    bil1 = int(file.readline())

    #baca baris kedua dari file
    #simpan ke dalam variabel bil2 sebagai integer
    bil2 = int(file.readline())

    #hitung dan tampilkan hasil bagi
    hasil= bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)
    
except ZeroDivisionError:
    print ('Tidak Boleh Pembagian Dengan Nol')
except FileNotFoundError:
    print ('File Tidak Ditemukan')
