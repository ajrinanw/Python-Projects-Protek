#PHYTON PROJECT 01

#manual
def ubahHuruf(teks, a, b) :
    Teks = list(teks)
    for i in range(len(Teks)) :     
        if(Teks[i] == a) :
            Teks[i] = b
    ganti = ''.join(Teks)
    return ganti

#withreplace
def ubahhuruf(teks, a, b) :
    ganti = teks.replace(a, b)
    return ganti

teks = input("Masukkan kata / kalimat yang anda ingin ubah : ")
a = input("Masukkan huruf / kata apa yang ingin anda ubah : ")
b = input("Ubah {} menjadi : ".format(a))

Hasil = ubahHuruf(teks, a, b)
print(Hasil)

hasil = ubahhuruf(teks, a, b)
print(hasil)
