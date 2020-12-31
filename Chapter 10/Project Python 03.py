#PHYTON PROJECT 03

file = open('fileData.txt', 'r')
line = file.readlines()
data = {}

for i in range(len(line)) :
    a = line[i].split('|')
    a[2] = a[2].replace('\n', '')
    
    data[i] = {'nim' : a[0], 'nama' : a[1], 'alamat' : a[2]}

print(data)
