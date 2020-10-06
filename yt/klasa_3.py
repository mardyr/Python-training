class Ksiazka:
    def __init__(self,tytul,autor,rok="2019"):
        '''

        :param tytul: Podaj tytul
        :param autor: Podaj autora
        :param rok: Podaj rok
        '''
        print("Uruchomiono konstruktor klasy Książka")
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.__priv = 1 # zmienna prywatna , czyli tylko do klasy, obiekt nie ma dostepu, niby , bo mozna
        # obiekt._Ksiazka__priv


    def __del__(self):
        print("End of the road")

k = Ksiazka ("Feeling","Jucewicz")
print(k.rok)
try:
    print(k._Ksiazka__priv)
except Exception as e:
    print("Nie udalo sie wywolac, poniewaz",e)

