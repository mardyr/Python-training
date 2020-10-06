import os

lista = os.listdir("..")
for i in lista:
    if os.path.isfile(os.path.join("..", i)): print("{} jest plikiem".format(i))
    if os.path.isdir(os.path.join("..",i)): print("{} jest directory".format(i))
open("rad.txt","w").close()
if os.path.exists("nowy folder"):
    print("Istnieje")

#if not os.path.exists("Moja sciezka"):
   # os.mkdir("Moja sciezka")

#os.removedirs("Moja sciezka")
#os.rename("pliki","nowy folder")


path = "pliki/01/danew.txt"

file = open("test.txt","w")
file.close()

dirpath = os.path.dirname(path)  # tworzy nam sciezke do ostaniego , czyli pliki/01
if not os.path.exists(dirpath):
    os.makedirs(dirpath)
file = open(path,'w')

