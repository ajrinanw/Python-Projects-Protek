#CHAP.05 PRAK.02 LATIHAN 05

from random import randint
bil = randint(0,100)

print("Hi.. Nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 1 sampai dengan 100. Silahkan tebak ya..!!")


tebakan = int(input("Tebakan Kamu :"))

while True:
    if (tebakan > bil):
        print ("Yahhh tebakan mu terlalu besar, coba lagi")
        tebakan = int(input("Tebakan Kamu :"))
    elif (tebakan < bil):
        print ("Yahhh tebakan mu terlalu kecil, coba lagi")
        tebakan = int(input("Tebakan Kamu :"))
    else :
        print ("Yeayy tebakan mu BENAR")
        break

