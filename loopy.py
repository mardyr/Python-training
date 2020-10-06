fruits = ["apple","orange","peach","cherry","plum","banana"]

print("Start loop")

for i,fruit in enumerate(fruits):
    print("Sprawdzam {}".format(i))
    if i==3 : break
    print("{} jest ok.".format(fruit))

print("Koniec")

x = "Hello {} {}"
y = x.format("World",5)
print(x)
print(y)


lista = [1,3,"A","Dom",2.3]
print(lista[0])
lista[0] = "wiadra"
print(lista[0])
print(lista[0:4])
print(lista)
lista.pop()
lista.insert(2,43.2)
print(lista)
del lista[3]

lista.clear()

lista.insert(0,20)
print(len(lista))

lista3 = list(range(0,100,2))

lista4 = lista3[0:25:3]+lista

print(lista4)