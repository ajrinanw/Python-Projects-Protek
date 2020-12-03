#CAHPTER 08 PYTHON PROJECT 04
sayur = ['bayam', 'kangkung', 'wortel', 'selada']

def tambahSayur() :
    sayurAdd = input("Masukkan nama sayur yang ingin ditambahkan : ").lower()
    sayur.append(sayurAdd)
    return sayur

def hapusSayur() :
    sayurDel = input("Masukkan nama sayur yang ingin dihapus : ").lower()
    if(sayurDel in sayur) :
        sayur.remove(sayurDel)
    else :
        print("Sayur tersebut tidak terdapat dalam data")
    return sayur

def liatSayur() :
    print(sayur)


print("Ada Yang Bisa Kami Bantu ? : ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("D. Keluar")

while True :
    pilihan = input("Pilihan Anda : ")
    if(pilihan=='A' or pilihan=='a') :
        tambahSayur()     
    elif(pilihan=='B' or pilihan=='b') :
        hapusSayur()
    elif(pilihan=='C' or pilihan=='c') :
        liatSayur()
    elif(pilihan=='D' or pilihan=='d') :
        break   
    else :
        print('Input Invalid')
        continue
