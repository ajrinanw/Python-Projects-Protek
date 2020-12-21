#PHYTON PROJECT 07

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listupgrade = []

for i in range(len(mhs)) :
    x = mhs[i].split(':')
    listupgrade.append(x)

    y = listupgrade[i][2].split('-')
    y.reverse()
    
    ygabung = '/'.join(y)
    listupgrade[i][2] = ygabung

print('=' * 65)
print('NIM'.ljust(11), 'NAMA MAHASISWA'.ljust(22), 'TGL LAHIR'.ljust(17), 'TEMPAT LAHIR'.ljust(20))
print('-' * 65)

for i in range(len(listupgrade)) :
    print(listupgrade[i][0].ljust(11), listupgrade[i][1].ljust(22), listupgrade[i][2].ljust(17), listupgrade[i][3].ljust(20))
print('-' * 65)
