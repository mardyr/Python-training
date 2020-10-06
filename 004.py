# zestaw niezmienialnych obiektow
krotka = ('v',5,'string')
print(krotka[0],krotka[1],type(krotka),type(krotka[2]),sep='\t')

tuple1 = tuple(range(0,100,5))
print(tuple1,type(tuple1),sep=":")

# lista, krotka ktora mozna zmieniac
lista = ['lol',2,'A']
print(lista[0])
lista[0] = 22
print(lista[0])
print("lista: ",lista,type(lista))

lista2 = []
lista2.append(123)
lista2.append(1)
lista2.append(10)

print(lista2)
print(max(lista2),min(lista2))
print('1:2',lista2[1:3]) # wyswietlam fragment listy od 1 do 3 (bez 3)
lista2.insert(0,100)
print('przed reverse',lista2)
lista2.reverse()
print('reverse',lista2)
lista2.pop()
print('pop',lista2)
del lista2[1] # usuwam 2 element z listy
print("del",lista2,sep=';;')

lista2.clear() # czyszcze liste, lista pusta
print(lista2,':lista2')
lista2.append(10)
lista2.append(-12)
lista2.insert(0,40)
print(lista2)
print(len(lista2)) # ile elementów na liscie
lista3 = list(range(1,100))
lista4 = lista3[1:25:3]+lista2
print(lista4)
print("Ile razy 20",lista4.count(20),sep=' - ')
lista5 = [5]*10
