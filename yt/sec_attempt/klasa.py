class Book:
    def __init__(self,title,author,year = "2019"):
        print("Uruchomiono konstuktor")
        self.title = title
        self.author = author
        self.year = year
        self.__priv = 1

    def __del__(self):
        print("kaBUUUM")


book = Book("C++","Zelent")

try:
    print(book.__priv)
except Exception as e:
    print("Nie udało się wywołać book, bo ",e)

print(book._Book__priv)

del book


class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self._alfa = None
        self.__beta = "mystery"
    def __str__(self):

        return f'zmienne to x = {self.x}, y = {self.y}, beta = {self.__beta}'
    @staticmethod
    def metoda_statyczna():
        print("Funkcja statyczna")
        return True
    def __metoda_chroniona(self):
        return True
    @property # taki getter tylko zwraca
    def alfa(self):
        print("Pobieramy wartosc")
        return self._alfa
    @alfa.setter # ustawia wartosc
    def alfa(self,value):
        print("Ustawiam wartosc")
        self._alfa = value
    @alfa.deleter
    def alfa(self):
        print("Ppapapa")
        del self._alfa
    @property
    def beta(self):
        return self.__beta



p = Point(2,4)
print(p)
Point.metoda_statyczna()
p.value = 12*100
print(p.value)

print(p.alfa)
p._alfa = 20
print(p.alfa)
p.alfa = 99
print(p.alfa)

del p.alfa

print(p.beta)


