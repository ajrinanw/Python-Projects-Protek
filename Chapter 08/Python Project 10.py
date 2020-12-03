#CAHPTER 08 PYTHON PROJECT 10
listBuah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

def jumlahBuah():
    jumlah=int(input('Masukkan jumlah Kg yang diinginkan : '))
    harga=listBuah.get(namaBuah, 0)*jumlah
    return harga

print("List buah yang tersedia : ")

for x,y in listBuah.items() :
    print("- ", x, ":", y)

totalHarga=[]

i=True
while (i==True):
    namaBuah = input("Masukkan nama buah yang akan dibeli : ").lower()
    
    if(namaBuah not in listBuah.keys()) :
        print("Maaf, buah yang anda masukkan tidak tersedia")
        continue

    else :
        try :
            harga=jumlahBuah()
            totalHarga.append(harga)

            lanjut=input("Input Nama Lagi ? (y/n) : ").lower()
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
