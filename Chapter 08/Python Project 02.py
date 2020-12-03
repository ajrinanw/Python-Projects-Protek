#CAHPTER 08 PYTHON PROJECT 02
def dataStat(x) :
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    dataStatistika=[a,b,c]
    return dataStatistika

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

hasil=dataStat(data)
print(hasil)

