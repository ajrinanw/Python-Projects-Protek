#CAHPTER 08 PYTHON PROJECT 03
data=[]

i=True
while(i==True):
    nama=input("Masukkan Nama Mahasiswa : ")
    data.append(nama)
    lanjut=input("Input Nama Lagi ? (y/n) : ")

    if(lanjut=="y"):
            i=True   
    elif(lanjut=="n"):
            i=False
    else:
        print("Input Invalid")
        break

print()
data.sort()

for x in range(len(data)) :
    print(data[x], "(", len(data[x]), "karakter )")
