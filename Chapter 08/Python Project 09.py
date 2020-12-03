#CAHPTER 08 PYTHON PROJECT 09
listBuah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

def jumlahBuah():
    jumlah =int(input('Massukkan jumlah Kg yang diinginkan : '))
    print("--------------------------------------------")
    print("Total Harga : ", listBuah.get(namaBuah, 0)*jumlah)

print("List buah yang tersedia : ")

for x,y in listBuah.items() :
    print("- ", x, ":", y)

while True :
    namaBuah = input("Masukkan nama buah yang akan dibeli : ")
    
    if(namaBuah not in listBuah.keys()) :
        print("Maaf, buah yang anda masukkan tidak tersedia")
        continue

    else :
        while True :
            try :
                jumlahBuah()
                break
            except ValueError :
                continue
        break


