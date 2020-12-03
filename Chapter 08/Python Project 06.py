#CAHPTER 08 PYTHON PROJECT 06
def sortStringByChar(data) :
    data.sort(reverse=True)
    return data

data = ['apel', 'rambutan', 'jeruk']
dataTersort = sortStringByChar(data)

print("Data baru terurut dengan karakter terbanyak ke terkecil : ", dataTersort)
