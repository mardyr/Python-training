#Generacja liczb parzystych
for i in range(2,101,2):
    print(i,end=" ")

print('\n','*'*100)

def CollectParity(a,b):

    for i in range(a+1 if a%2 else a,b+1,2):
        print(i,end = ' ')
    print('\n',"*"*50)

CollectParity(2,31)
# Porównanie iteracji i rekurencji
import time

c1 = time.time()

Z = [1,1]
for i in range(1,29):
    Z.append(Z[len(Z)-1]+Z[len(Z)-1])
print(Z)
c2 = time.time()
print("Czas iteracji: ",c2-c1)

def fibrek(n):
    return fibrek(n-1)+fibrek(n-2) if n>2 else 1
c3 = time.time()
for i in range(1,31):
    print(fibrek(i),end =' ')
c4 = time.time()
print("\nCzas rekurencji: ",c4-c3)

# Kwadrat zbudowany z losowej małej literki dla \
#losowego n>4. Kwadrat ma być w wersji wypełnionej i pustej

import random
n = random.randint(5,10)
print('n=',n)

kod = random.randint(97,97+25)
literka = chr(kod)

for i in range(1,n+1):
    print(literka*n)
print('*'*50)

for i in range(1,n+1):
    if(i==1 or i==n): print(n*literka)
    else : print(literka," "*(n-4),literka)

# Stworz funkcje otrzymujaca słownik i zwracajaca jego czesc
# zlozona z czesci klucz - wartosc, gdzie klucz nie jest liczbą

S = {'klucze':100,'klucz2':200,1:'słoń',5:'kasza','klucz':300}

for k,v in S.items():
    print(k,':',v)

def reduceDictionary(Dict):
    newDict = {k: v for k,v in Dict.items()
        if not(isinstance(k,int) or isinstance(k,float))}
    return newDict

print(reduceDictionary(S))