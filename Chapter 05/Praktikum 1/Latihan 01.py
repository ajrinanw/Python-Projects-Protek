#CHAP. 05 PRAK. 01 LATIHAN 01

bahasaIndo = int(input("Nilai Bahasa Indonesia : "))
if (bahasaIndo >= 0) and (bahasaIndo <= 100):
    mat = int(input ("Nilai Matematika : "))
    if (mat >= 0) and (mat <= 100):
        ipa = int(input("Nilai IPA : "))
        if (ipa >= 0) and (ipa <= 100):
            print ("---------------------------")
else:
    print("Masukkan nilai dengan range 0-100")

if (bahasaIndo >= 60) and (mat > 70) and (ipa >= 60):
    print ("Status  Kelulusan : LULUS")
else :
    print ("Status  Kelulusan : TIDAK LULUS")
              
