#PHYTON PROJECT 06

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("=" * 65)
print("NIM".ljust(10), "NAMA".ljust(10), "N.MID".rjust(10), "N.UAS".rjust(10), "N.AKHIR".rjust(10), "STATUS".rjust(10))
print("-" * 65)

for i in nilai :
    finalscore = (i['mid'] + (2*i['uas'])) / 3
    finalscore = int(finalscore)

    if(finalscore >= 60) :
        status = "LULUS"
    else :
        status = "TIDAK LULUS"
    print(i['nim'].ljust(10), i['nama'].upper().ljust(10),  str(i['mid']).rjust(10),  str(i['uas']).rjust(10), str(finalscore).rjust(10),  status.rjust(10))
print("-" * 65)
