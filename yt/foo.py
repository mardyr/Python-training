
def test(tekst):
    print("Test: ",end=" ")
    print(tekst)


def suma(x,y):
    return x+y

def apple(tekst):
    print("Apple: ",end=" ")
    print(tekst)

with open("dane.txt","a+") as file:
    file.seek(0)
    for line in file:
        print(line.strip())

import pickle
lista = [1,3,4,"Koster",2.2]
with open("plik.pickle","wb") as output:
    pickle.dump(lista,output)

with open("plik.pickle","rb") as inputfile:
    unpacked = pickle.load(inputfile)
    print(unpacked,type(unpacked))