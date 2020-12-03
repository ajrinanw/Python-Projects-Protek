#CHAP.07 PRAK.03 LATIHAN 01
try:
    file = input('Masukkan nama file :')
    print ('Isi File', file, 'adalah :')
    print (open (file,'r').read())
except FileNotFoundError:
    print ('Maaf File Tidak Ditemukan')
except UnicodeDecodeError:
    print ('Maaf File Tidak Dapat Diakses')
