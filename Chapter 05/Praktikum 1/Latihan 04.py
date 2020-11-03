#CHAP. 05 PRAK. 01 LATIHAN 04

kode = int(input("Masukkan kode karyawan :"))
nama = input("Masukkan nama karyawan :")
gol  = input("Masukkan golongan      :")

print ("========================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("----------------------------------------")
print ("Nama Karyawan  :", nama, "(Kode :", kode, ")")
print ("Golongan       :", gol)
print ("----------------------------------------")

if (gol=="A"):
    gajiPokok = 10000000.0
    pot = 2.5
    potongan = 2.5/100*gajiPokok
    gajiBersih = gajiPokok - potongan
elif (gol=="B"):
    gajiPokok = 8500000.0
    pot = 2
    potongan = 2/100*gajiPokok
    gajiBersih = gajiPokok - potongan
elif (gol=="C"):
    gajiPokok = 7000000.0
    pot = 1.5
    potongan = 1.5/100*gajiPokok
    gajiBersih = gajiPokok - potongan
elif (gol=="D"):
    gajiPokok = 5500000.0
    pot = 1
    potongan = 1/100*gajiPokok
    gajiBersih = gajiPokok - potongan
elif (gol=="a")or(gol=="b")or(gol=="c")or(gol=="d"):
    print ("Gunakan huruf kapital!")
else:
    print ("Golongan anda tidak valid")
    

print ("Gaji Pokok     : Rp ", gajiPokok)
print ("Potongan(", str(pot), "%): Rp", potongan)
print ("----------------------------------------")
print ("Gaji Bersih    : Rp", gajiBersih)
