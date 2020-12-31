#PHYTON PROJECT 02

file = open('fileData.txt', 'a+')

i = True
while ( i == True) :
    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")

    file.write(nim + "|" + namaMhs + "|" + alamat + "\n")  
    ulang = input("Ulangi input lagi (y/n) : ")
    
    if (ulang == "y") :
        i = True
    elif  (ulang == "n"):
        i = False
    else :
        print ("Inputan anda invalid")
        continue
    
file.seek(0,0)
isi = file.read()
print (isi)
file.close()
