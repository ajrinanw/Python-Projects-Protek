#CAHPTER 08 PYTHON PROJECT 12
listBuah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

def jumlahBuah(daftarBuah,namaBuah):
    jumlah=int(input('Massukkan jumlah Kg yang diinginkan : '))
    harga=daftarBuah.get(namaBuah, 0)*jumlah
    return harga

def beliBuah(daftarBuah):
    print("List buah yang tersedia : ")

    for x,y in daftarBuah.items() :
        print("- ", x, ":", y)

    totalHarga=[]

    i=True
    while (i==True):
        namaBuah = input("Masukkan nama buah yang akan dibeli : ").lower()
    
        if(namaBuah not in daftarBuah.keys()) :
            print("Maaf, buah yang anda masukkan tidak tersedia")
            continue

        else :
            try :
                harga= jumlahBuah(daftarBuah,namaBuah)
                totalHarga.append(harga)

                lanjut=input("Ingin buah yang lain ? (y/n) : ").lower()
                if(lanjut=="y"):
                    i=True   
                elif(lanjut=="n"):
                    i=False
                else:
                    print("Input Invalid")
                    break
            except ValueError:
                print("Input Invalid")
                continue
            
    print("--------------------------------------------")
    print ("Total Harga : ", sum(totalHarga))

def tambahBuah(daftarBuah) :
    buahAdd = input("Masukkan buah yang ingin ditambahkan : ").lower()

    while True :
        try : 
            if(buahAdd in daftarBuah.keys()) :
                print("Buah ", buahAdd, "Buah sudah ada di dalam data. Silakan masukkan harga terbaru")
                hargaNew = int(input("Masukkan harga satuan buah : "))
                
                daftarBuahBaru = {buahAdd : hargaNew}
                daftarBuah.update(daftarBuahBaru)
                
                print("List buah yang tersedia : ")

                for x,y in daftarBuah.items() :
                    print("- ", x, "(harga : ", y, ")")

            else :
                hargaNew = int(input("Masukkan harga satuan : "))
                listBuah[buahAdd] = hargaNew
                
                print("List buah yang tersedia : ")

                for x,y in daftarBuah.items() :
                    print("- ", x, "(harga : ", y, ")")
            break

        except ValueError :
            print("Input Invalid")
            continue
        
def hapusBuah(daftarBuah) :
    buahDel = input("Masukkan nama buah yang ingin anda hilangkan : ").lower()

    if(buahDel in daftarBuah.keys()) :
        del daftarBuah[buahDel]
        print("Buah ", buahDel, "berhasil dihapus dari data")
        
        print("Data Buah : ")
        for x,y in daftarBuah.items() :
            print("- ", x, "(harga : ", y, ")")
    else :
        print("Maaf, buah yang anda masukkan tidak tersedia")

print("Ada yang dapat kami bantu ? : ")
print("A. Tambah data buah")
print("B. Beli buah")
print("C. Hapus data buah")
print("D. Keluar")

while True :
    pilihan= input("Pilihan anda : ").lower()
    
    if(pilihan == 'A' or pilihan == 'a') :
        tambahBuah(listBuah) 
    elif(pilihan == 'B' or pilihan == 'b') :
        beliBuah(listBuah)
    elif(pilihan == 'C' or pilihan == 'c') :
        hapusBuah(listBuah)
    elif(pilihan == 'D' or pilihan == 'd') :
        break
        
    else :
        print("Input Invalid")
        continue
