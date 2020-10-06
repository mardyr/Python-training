#zapis do pliku
fd = open('dane.txt','w',encoding="utf-8") # kodowanie na polskie znaki
fd.write("Pierwsza linia tekstu w pliku śćźńąłć.\n")
fd.write("Druga linia tekstu w pliku. \n")
fd.write("Trzecia linia tekstu w pliku.\n")
fd.close() # zamykam plik

import os # operacje na plikach/ katalogach

#odczytanie z pliku

def myReadFile(path):

    if os.path.isfile(path):
        fdread = open(path,'r',encoding="utf-8")
        lines = list(map(lambda line: line.strip(),fdread))
        # do lines zapisuje po kolei kazda linie , obcinajac biale znaki
        print(lines,sep='@')
    else :
        print("Plik",path," nie istnieje")

myReadFile("dane.txt")


if os.path.isfile("dane.txt"):
    fdread = open("dane.txt","r",encoding = "utf-8")
    fdtotal = fdread.read()
    print(fdtotal)
    fdread.seek(0)
    lines = fdread.readlines()
    print(lines)
    fdread.close()

try:
    L = ['A','B','\nC']
    with open('dane.txt','a',encoding="utf-8")as fd:   # automatycznie zamkniecie pliku
        for elem in L :
            fd.write(elem)
except:
    print("Zanim przekazano tu wyjątek konstrukcja with wymusiła zamknięcie zasobów")
    fd.read()


def myReadFilee(path):
    if os.path.isfile(path) :
        with open(path,'a',encoding="utf-8") as fread:
            for lines in fread:
                print(lines,sep="@")
    else:
        print("Plik",path,"nie istnieje")

myReadFilee("dane.txt")


lista = [10,20,'trzydzieści',[1,2,"trzy"]]
with open('plik.pickle','wb') as outPut:
    pickle.dump(lista,outPut)
    outPut.close()