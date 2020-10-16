'''
lista = ['czesc','to','ja','kto']

with open('test.txt','w') as plik:
    for i in lista:
        #print(i,file=plik) # metoda przechodzenia do nowej linii
        plik.write(i)
        plik.write(' ')
with open('test.txt','a') as plik:
    print("test",file = plik)
'''
import csv
pola = [] # nazwa kolumn
wiersze = [] # zawartosci kolumn
with open('Zeszyt.csv') as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter = ';')

    pola = next(czytnikCSV)

    wiersze = [wiersz for wiersz in czytnikCSV ]
    print(pola)
    print(wiersze[0])

    # liczymy srednia
    suma = 0
    for wiersz in wiersze:
        suma = suma + float(wiersz[2])
    srednia = suma / len(wiersze)
    print(round(srednia, 2))

with open("Zeszyt.csv",mode = 'w') as plikCSV:
    pola = ['pracownik','stanowisko','pensja']
    lista = [{'pracownik':'Jan','stanowisko':'biegacz','pensja':'1000'},
             {'pracownik':'Brokul','stanowisko':'dietetyk','pensja':'8000'},
              {'pracownik':'James','stanowisko':'dyrektor','pensja':'20000'}]
    writer = csv.DictWriter(plikCSV, fieldnames=pola)
    writer.writeheader()
    for x in lista:
        writer.writerow(x)