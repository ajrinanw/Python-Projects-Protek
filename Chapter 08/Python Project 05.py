#CAHPTER 08 PYTHON PROJECT 05
def kuadrat(bil) :
    bilangan = []
    for i in range(len(bil)) :
        a = bil[i]*bil[i]
        bilangan.append(a)
    return bilangan

dataBil = [2, 4, 5, 6]
hasil = kuadrat(dataBil)
print(hasil)
