#CAHPTER 08 PYTHON PROJECT 11
listBuah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

def jumlahBuah(namaBuah):
    jumlah=int(input('Massukkan jumlah Kg yang diinginkan : '))
    harga=listBuah.get(namaBuah, 0)*jumlah
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
                harga= jumlahBuah(namaBuah)
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
        
print("Ada yang dapat kami bantu ? : ")
print("A. Tambah data buah")
print("B. Beli buah")
print("C. Keluar")

while True :
    pilihan= input("Pilihan anda : ").lower()
    
    if(pilihan == 'A' or pilihan == 'a') :
        tambahBuah(listBuah) 
    elif(pilihan == 'B' or pilihan == 'b') :
        beliBuah(listBuah)
    elif(pilihan == 'C' or pilihan == 'c') :
        break
        
    else :
        print("Input Invalid")
        continue
