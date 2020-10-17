
#tarif
tarif_awal=200000
tarif_lanjutan=10000

#waktu
jam_start=6
jam_finish=23
menit_start=0
menit_finish=50

jam_total=jam_finish-jam_start
menit_total=(menit_finish-menit_start)//60
total_waktu=jam_total+menit_total

#biaya
biaya=(10000*(total_waktu-12))+200000

print ("total tarif yang harus dibayarkan kepada rental mobil sebesar",biaya, "ribu rupiah")
