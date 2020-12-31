#PHYTON PROJECT 04

file = open('fileData.txt', 'r')
cariNim = input("Masukkan NIM yang mau dicari : ")
line = file.readlines()

for i in range(len(line)) :
    a = line[i].split('|')

    if(cariNim in line[i]) :
        status = 'ada'
        print("Data Mahasiswa ")
        print("NIM    : ", a[0])
        print("Nama   : ", a[1])
        print("Alamat : ", a[2])
        break

    else :
        status = 'tidak ada'

if (status == 'tidak ada'):
    print("Data Mahasiswa Tidak Ditemukan")
file.close()
