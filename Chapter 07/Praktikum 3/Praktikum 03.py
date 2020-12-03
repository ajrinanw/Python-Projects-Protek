#CHAPTER 07 PRAKTIKUM 03

file = open('C:/Users/asus/Documents/Python Projects/Python-Projects-Protek/Chapter 07/Praktikum 3/data.txt','r')
sum = 0
for data in file:
    try :
        sum = sum+int(data)
    except ValueError :
        continue
print(sum)

