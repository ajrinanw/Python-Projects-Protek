#CHAP.05 PRAK.01 LATIHAN 05

kode  = int(input("Masukkan kode karyawan :"))
nama  = input("Masukkan nama karyawan :")
gol   = input("Masukkan golongan      :")
status= input("Masukkan Status (1:Menikah,2:Belum Menikah):")
if (status=="1"):
    statusMenikah = "Menikah"
    anak = int(input("Masukkan Jumlah Anak   :"))
    tPasangan = 10
    tAnak = 5
else:
    statusMenikah = "Belum Menikah"
    anak = 0
    tPasangan = 0
    tAnak = 0

print ("========================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("----------------------------------------")
print ("Nama Karyawan :", nama, "(Kode :", kode, ")")
print ("Golongan      :", gol)
print ("Status Menikah:", statusMenikah)
print ("Jumlah Anak   :", anak)
print ("----------------------------------------")

if (gol=="A"):
    gajiPokok = 10000000.0
    pot = 2.5
    potongan = pot/100*gajiPokok
    tunjanganPasangan = tPasangan/100*gajiPokok
    tunjanganAnak = tAnak/100*gajiPokok
    gajiKotor = gajiPokok+tunjanganPasangan+tunjanganAnak
    gajiBersih = gajiKotor - potongan
elif (gol=="B"):
    gajiPokok = 8500000.0
    pot = 2
    potongan = pot/100*gajiPokok
    tunjanganPasangan = tPasangan/100*gajiPokok
    tunjanganAnak = tAnak/100*gajiPokok
    gajiKotor = gajiPokok+tunjanganPasangan+tunjanganAnak
    gajiBersih = gajiKotor - potongan
elif (gol=="C"):
    gajiPokok = 7000000.0
    pot = 1.5
    potongan = pot/100*gajiPokok
    tunjanganPasangan = tPasangan/100*gajiPokok
    tunjanganAnak = tAnak/100*gajiPokok
    gajiKotor = gajiPokok+tunjanganPasangan+tunjanganAnak
    gajiBersih = gajiKotor - potongan
elif (gol=="D"):
    gajiPokok = 5500000.0
    pot = 1
    potongan = pot/100*gajiPokok
    tunjanganPasangan = tPasangan/100*gajiPokok
    tunjanganAnak = tAnak/100*gajiPokok
    gajiKotor = gajiPokok+tunjanganPasangan+tunjanganAnak
    gajiBersih = gajiKotor - potongan
elif (gol=="a")or(gol=="b")or(gol=="c")or(gol=="d"):
    print ("Gunakan huruf kapital!")
else:
    print ("Golongan anda tidak valid")

print ("Gaji Pokok    : Rp ", gajiPokok)
print ("Tunjangan Istri/Suami: Rp", tunjanganPasangan)
print ("Tunjangan Anak: Rp ", tunjanganAnak)
print ("----------------------------------------+")
print ("Gaji Kotor    : Rp", gajiKotor)
print ("Potongan      : Rp", potongan)
print ("-----------------------------------------")
print ("Gaji Bersih   : Rp", gajiBersih)





