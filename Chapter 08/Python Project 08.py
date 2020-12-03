#CAHPTER 08 PYTHON PROJECT 08
buah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

def rataHarga(buah):
    jumlahX=0
    n=0
    for x,y in buah.items():
        jumlahX+=y
        n+=1
    ratarata = jumlahX/n
    return ratarata

hasil=rataHarga(buah)

print("Rata-rata harga buah adalah", hasil)
