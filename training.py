'''
from random import randint

x = randint(1,10)
print("x value",x)

from random import random

y = random()
print(y)

import math as m


z = m.sin(60)

print(z)

z = "188"
i = 12 + int(z)
print(i)

z1 = str(i)
print(z1,type(z1),sep='::')

print(z,i,'-'*50,end='\t*')

lista = [0,"1",'sfd']
print("\n",lista)
print("\n",lista[1])
lista.pop()
lista.append(112)
lista.append(23)
lista.append(2)
print(lista)
print(lista[0:4])
lista3 = list(range(1,30))
print(lista3)
lista4 = lista3[9:25:5]+lista
print(lista4)
del lista4[2]
print(lista4)
lista4.clear()
print(lista4)

krotka = (1,2.3,True)
print(krotka)
print(krotka[1])
'''
'''
kr = tuple(range(1,20))
print(kr)
kro = (1,"str",2.3,True)
print(kro)

print(kro[1:3]+kr[1:8])

ls = list(range(1,25))

print(max(ls),min(ls))
ls.reverse()
ls.insert(0,-23)
ls.append(43)
print(ls)
del ls[1]
print("Przed delem" , ls)
print("Ile jest 20 ", ls.count(20))
print(len(ls))
'''
i = 13;
c =3.2 if i<10 else 11.12 if i>15 else 1.12 #  if i< 10 c = 3.2 , else if(i>15) c = 11.12 else c=1.12
print("c= ",c) # c = 1.12

while i :
    print(i)
    i-=1
z =3
tup = (1,3,4,2,3,4,5)
if z in tup :
    print("I get you")

directory = {'a':1.1,'b':1.2,'c':1.3,'d':1.4}
for x in directory:
    print(x,"",directory[x],sep=" ")

if 24<21:
    print("SAY WHAAT?")
else :
    print("LOGIC IS HERE ")

j = 20
while j :
    if(j%2):
        j-=1
        continue
    print(j)
    j -= 1
