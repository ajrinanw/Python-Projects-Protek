#PHYTON PROJECT 01

from datetime import *

def diffDate(x) :
    tanggal = x.split("-")
    dateList = []

    for i in tanggal :
        dateList.append(int(i))

    past = date(dateList[0], dateList[1], dateList[2])
    now = datetime.date(datetime.now())

    hasil = past - now
    result = (hasil.days)

    return result

'''
#mencoba function
print(diffDate('2018-12-30'))
print(diffDate('2021-01-20'))


try :
    ans = input("Masukkan tanggal (yyyy-mm-dd) : ")
    hasil = diffDate(ans)
    print("Selisih tanggal {0} dengan hari ini adalah {1} hari".format(ans, hasil))
    print ("\nnb. (-) memiliki arti hari sudah lampau")
except ValueError :
    print("Input Invalid")
'''
