#PHYTON PROJECT 01

file = open('fileAngka.txt','r')
line = file.readlines()

genap = []
ganjil = []

for i in range(len(line)) :
    print(line[i])
    
    if(int(line[i])%2 == 0) :
        genap.append(line[i])
    else :
        ganjil.append(line[i])


print("Banyaknya bilangan genap  : {0}".format(len(genap)))
print("Banyaknya bilangan ganjil : {0}".format(len(ganjil)))

file.close()
