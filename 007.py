# FUNKCJA

# def funkcja(arg):
#   '''dokumentadja - co ta funkcja robi'''
#   kod

# nie ma argumentów, nic nie zwraca
def nic():
    pass

nic()
nic()

def ileCzego(arg1,arg2='default'):
    arg1 = int(arg1) # na wszelki konwertujemy to na liczbe
    print((' '+arg2)*arg1)

ileCzego(3)
ileCzego(12.8,'*-')

f = ileCzego  # taka referencja teraz f to bedzie ileCzego
f(5,'*')

# eval funkcja, ktora interpretuje napisy jakby byly kodem napisanym w interpreterze
v = 'ileCzego'
x=10
tpl='#'
print(v+'('+str(x)+",tpl)")
eval(v+'('+str(x)+",tpl)")
polecenie = input("Podaj polecenie: ")
eval(str(polecenie))
from random import randint
def multi(arg1):
    return arg1*8
print(multi(2)*multi(4))

def fnc(a,b):
    z = a*b+b
    return z

zmi = 34.3
zm1 = 21.2
eval('fnc('+str(zmi)+','+str(zm1)+')')

var = 3
var1 = 10
def changeGlobal() :
    var2 = 100
    global var
    var = 2
    var1 = 11

changeGlobal()
print('var',var,'var1',var1)

def collectionReturn():
    return(1,2,'3')
a,b,c = collectionReturn()
print(a,b,c,type(c))

def collectionReturn():
    return {'a':1,'b':20,'c':321}

print(collectionReturn()['c'])

def multiArgs(*args):
    suma = 0
    for i in args:
        print(i)
        if(isinstance(i,int) or isinstance(i,float)): suma+=i
    return suma

print('multiArgs(1,2,3)=',multiArgs(1,2,3))

nums = (1,2,3,4,5,0.5,'rabarbar') #rozpakowywanie krotki
suma = multiArgs(*nums)
print('suma',suma)

# LAMBDA - funkcje anonimowe, tam gdzie funkcja zamiast argumentu w innej funkcji
f = lambda arg : arg+1
print('lambda f(5)',f(5))

g = lambda x,y,z : (x+y)*z

print('g(1,2,3)',g(1,2,3))

h = lambda arg1 : 'jestem dodatnia' if arg1>0 else 'jestem niedodatnia'
print(h(5),h(-5),sep='|')

# map , dla kazdego elementu ze zbioru wywoluje funkcje

L = [1,2,3,4]

newL = map(lambda x:x+1,L) # newL to zwrocony przez map, specjalny iterator
# teraz ten iterator rzutujemy
print(list(newL))

# filter - funkcja ktora filtruje, czyli z pewnego zbioru wybiera wartosci
# ze wzgledu na kryteria

L = list(range(1,11))
newL = filter(lambda x:x%2==0,L)
print(list(newL))


# redukcja elementow do jednego elementu
from functools import reduce
suma = reduce(lambda x,y:x+y,L) # wez dwa elementy i zamien do jednego , az osiagniemy jeden
print(suma)


# yield , taki prawie return, ale zapamietuje swoje ostatnie wywolanie, mozna zwrocic zbior wynikow

def yieldPresentation():

    yield 'a'
    yield 1
    yield 2.5
    yield (1,2,3)

for i in yieldPresentation():
    if(isinstance(i,tuple)):
        for temp in i:
            print('\t',temp)
        print('\t: ilość elementów',len(i))
    else: print(i)

print(list(yieldPresentation())) # wymuszenie uzycia funkcji az zwroci swoje yieldy