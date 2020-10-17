#jarak
kotaA_B=125
kotaB_C=256

#kecepatan
kec1=62
kec2=70

#waktu
start=6
istirahat=45
#waktu dijadikan menit
timeA_B=(kotaA_B/kec1)*60
timeB_C=(kotaB_C/kec2)*60

time_total=timeA_B+timeB_C+istirahat

#untuk mendapatkan waktu jam
time_totaljam=int(time_total//60)
#untuk mendapatkan waktu menit
time_totalmenit=int(time_total%60)

waktu_seluruh=str(time_totaljam)+str('.')+str(time_totalmenit)
waktu_final=start+float(waktu_seluruh)

print ("maka Pak Amin sampai di Kota C pada pukul", waktu_final)
