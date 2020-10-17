#input data mahasiswa
co=int(input("Berapa Jumlah Mahasiswa Laki-laki di Jurusan PTIK UNS?"))
ce=int(input("Berapa Jumlah Mahasiswa Perempuan di Jurusan PTIK UNS?"))

co1=int(co/10)
ce1=int(ce/10)

print("berikut merupakan grafik diagram batang horizontal yang merepresentasikan data jumlah anak Laki-Laki dan Perempuan dari mahasiswa PTIK UNS")
print("Laki-laki = ","*"*co1,"(",int(co),")")
print("Perempuan = ","*"*ce1,"(",int(ce),")")
