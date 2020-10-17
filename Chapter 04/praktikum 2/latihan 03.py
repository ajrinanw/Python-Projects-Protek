import math

#penentuan total bensin (latihan 02)
jarak=795
jarak_bensin=12
#----------------------------------

total_bensin=jarak/jarak_bensin

#kapasitas maksimum tangki
tangki=50

bensin_sisa=total_bensin-50
isi_bensin=math.ceil(bensin_sisa/50)

print("Pak Budi harus mengisi bensin minimal", isi_bensin, "kali sehingga dapat menyelesaikan perjalanannya")

