#CAHPTER 08 PYTHON PROJECT 01
while True:
    try:
        n=int(input("Berapa Bnyak Data Yang Ingin Anda Input ? (Input dalam angka) : "))
        break
    except ValueError:
        print("Input Invalid")
        continue
data=[]

i=0
while (i<n):
    try:
        bil=int(input("Masukkan Bilangan Bulat : "))
        data.append(bil)
        i+=1
    except ValueError:
        print("Input Invalid")
        
data.sort(reverse = True)
print("Urutan terbesar ke terkecil adalah", data)
