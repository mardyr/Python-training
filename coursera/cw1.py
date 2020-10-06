#1
#Pobieraj od uzytkownika liste slow tak dlugo, az wprowadzi on słowo : "end"
#Słowo mogą byc wprowadzane pojedynczo lub poprzez wpisanie wielu słow po spacji
#Pobrane słowa zapisz do pliku words.pickle za pomocą piklowania
#Napisz funkcje, ktora laduje te slowa z pliku i sortuje
lista = []

while True:
    word = input("Podaj słowo ")
    word = word.strip()
    if len(word) ==0: print("sam Enter? Wpisz cos");continue
    if word == "end": break
    word = word.split()
    lista+=word
    print(lista)

import pickle
with open("words.pickle","wb") as output:
    pickle.dump(lista,output)

def readfrom(filepath):
    with open(filepath,"rb") as inputfile:
        unpacked = pickle.load(inputfile)
        sort = sorted(unpacked)
        print(sort)

readfrom("words.pickle")