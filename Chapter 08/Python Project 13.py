#CHAPTER 08 PYTHON PROJECT 13
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaiAkhirTop(nilai):
    mid=[]
    uas=[]
    nilaiAkhir=[]
    top={}

    for x in nilai:
        final=(x['mid']+(2*x['uas']))/3
        nilaiAkhir.append(final)

    top=nilaiAkhir.index(max(nilaiAkhir))
    hasil={'nim' : nilai[top]['nim'],
           'nama' : nilai[top]['nama']}
    return hasil

a = nilaiAkhirTop(nilaiMhs)
print("Mahasiswa dengan nilai tertinggi adalah", a['nama'], "dengan NIM", a['nim'])
