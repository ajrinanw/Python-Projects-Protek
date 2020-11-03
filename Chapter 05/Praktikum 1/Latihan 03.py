#CHAP. 05 PRAK. 01 LATIHAN 03

bahasaIndo = int(input("Nilai Bahasa Indonesia : "))
mat = int(input ("Nilai Matematika : "))
ipa = int(input("Nilai IPA : "))
print ("---------------------------")

if (bahasaIndo < 0) or (bahasaIndo > 100):
    print("Maaf input anda tidak valid")
elif(mat < 0) or (mat > 100):
    print("Maaf input anda tidak valid")
elif(ipa < 0) or (ipa > 100):
    print("Maaf input anda tidak valid")
elif (bahasaIndo >= 60) and (ipa >= 60) and (mat > 70):
    print ("Status  Kelulusan : LULUS")
else :
    print ("Status  Kelulusan : TIDAK LULUS")
    print ("Sebab :")
    if (bahasaIndo < 60):
        print ("-Nilai Bahasa Indonesia kurang dari 60")
    if (mat < 70):
        print ("-Nilai Matematika kurang dari 70")
    if (mat >69 and mat <71):
        print ("-Nilai Matematika tidak memenuhi persyaratan")
    if (ipa < 60):
        print ("-Nilai IPA kurang dari 60")
    
