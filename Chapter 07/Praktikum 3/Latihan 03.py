#CHAP. 07 PRAK. 03 LATIHAN 03
print('------------------------------')
print('   PROGRAM HITUNG RATA-RATA   ')
print('------------------------------')
    
i = True
jumlahX = 0
n = 0
    
while(i == True):
    try :    
        bil = int(input('Masukkan bilangan bulat : '))
        jumlahX += bil
        n += 1
        
        opsi = input('Lagi (y/n)? : ')

        if(opsi == 'y') :
            i = True
            
        elif(opsi == 'n') :
            i = False

        else :
            print('Inputan Invalid')
            break

    except ValueError:
            print('Bukan Bilangan Bulat')
            continue
    
rata = jumlahX/n
print(' ')
print('Rata - ratanya adalah  : ', rata)
print('------------------------------')
    
