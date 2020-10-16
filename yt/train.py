lista = [4,2,5,3]


'''
lista.sort(reverse=True)

if 5 not in lista:
     print("Jest")
else:
    print("Nie ma")
'''

data = "From marcindyrdol@gmail.com Wed Sep 14 16:18:00 2020"
pos = data.find('@')
pos2 = data.find(' ',pos)
print(data[pos+1:pos2])