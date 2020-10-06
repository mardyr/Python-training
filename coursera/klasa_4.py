class Organizm:
    zdrowie = 100
    opis = "To żyje!"

print(Organizm.opis,'i ma',str(Organizm.zdrowie)+ '% zdrowia.')
# takie zmienne statyczne
o1 = Organizm()
print(o1.zdrowie,o1.opis)

o2 = Organizm()
o2.zdrowie = 200
print(o2.zdrowie,o2.opis)

class Ksiazka:
    def __init__(self,tytul,autor,rok='2019'):
        '''
            Podaj argumenty
        '''
        print("Uruchomiono konstruktor klasy Książka")
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.__priv = 1
    def __del__(self):
        print("****kaBUUUUM!!!***")

book = Ksiazka("Ruchome piaski","Ja")
print(book.autor," ",book.rok)

try:
    print(book.__priv)
except Exception as e:
    print("Nie udal sie wywolac book, poniewaz:",e)

print(book._Ksiazka__priv) # a jednak sie dostane

del book


class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self._alfa = None
        self.__beta = "tajemnica"

    def __str__(self):  # gdy chcemy wyswietlic obiekt wpisujemy obiekt a nam wypluwa to co w templacie
        '''
        funkcja jest wywolana gdy probuje bezposrednio wystwietlic obiekt jako obiekt np print(self)
        '''
        template = "<punkt[x = {},y={}],[*{}*]"
        return template.format(self.x,self.y,self.__beta)

    def metoda(self):
        print("Jestem metodą klasy Punkt")

    @staticmethod  # dekorator metoda statyczna
    def metoda_statyczna():
        print("Jestem instrukcją metody statycznej klasy")
        return True

    def __metoda_chroniona(self): # dostac sie do niej przez obiekt._NAZWA KLASU__metoda_chroniona()
        return True

    #dekorator zglasza wlasnosc,metoda udaje ceche, wywoluje metode jakby byla cecha
    @property
    def alfa(self):
        print("a tu pobieramy sobie alfę")
        return self._alfa

    # ustawia wlasnosc jako chroniona
    @alfa.setter
    def alfa(self,v):
        print("Zanim przypisze wartosc, moge wywolac too ")
        self._alfa = v

    @alfa.deleter
    def alfa(self):
        print("usuwamy")
        del self._alfa
    @property
    def beta(self):
        return self.__beta
    @beta.setter
    def beta(self,v):
        print("A masz setterze!")
        self.__beta = v

p1 = Punkt(y=5,x=1)
print(p1)
p2 = Punkt(8,2)
print(p2)
p1.metoda()
Punkt.metoda_statyczna()
try:
    p1.metoda_chroniona()
except Exception as e:
    print("wyjatek ",e)
    print("Tylko to: ",p1._Punkt__metoda_chroniona())

p1.wartosc = 12*100
print(p1.wartosc)

print(p2._alfa)
print(p2.alfa)
p2._alfa = 100
print(p2._alfa)
p2.alfa = 10
print(p2._alfa)

del p2.alfa
print(p2.beta)
p2.beta =20
print(p2.beta)