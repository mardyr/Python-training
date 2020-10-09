class B(object):
    klasowa = None
    def __init__(self,x=10):
        self.x = x
        print("Jestem konstruktorem klasy B wywołanym \
 przy tworzeniu obiektu klasy" + str(self.__class__))
class C(B):
    pass

b = B(5)
c = C(2)
d = C()
print(b.klasowa)
b.klasowa = 2 # zmieniam parametr dla obiektu
B.klasowa = 3 # zmieniam parametr dla całej klasy
print(b.x,c.x,d.x,B.klasowa,C.klasowa)

print('*'*80)
from klasy2 import *
class Kolo(Punkt):
    '''Opis klasy, będzie dostępny pod polem __doc__ dla każdego obiektu oraz samej klasy'''
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r = r
    def __str__(self):
        return super().__str__() + '{r='+str(self.r)+'}'

k1 = Kolo(10,24,120)
print(k1, k1.__class__, k1.__doc__, Kolo.__doc__, Kolo.mro(), sep='\n')
print('*'*80)

class KoloZycia(Kolo,Organizm):
    def __init__(self,x,y,r):
        Kolo.__init__(self,x,y,r)
        Organizm.__init__(self,50,'pięknie żyje')

    def __str__(self):
        return Kolo.__str__(self)+' '+Organizm.__str__(self)

k2 = KoloZycia(10,24,120)
print(k2)
print(KoloZycia.mro())
print(hasattr(k2,'opis'))
print(getattr(k2,'zdrowie',1))
print(getattr(k2,'zdrowie2','brak zmiennej ale coś sobie zwróce'))
 ## ASERCJA TO TAKI TEST, sprawdzam czy obiekt jest tym co jest

x = 10
try:
     assert x == 12
except:
    print("mylisz się x to nie jest 12")

try:
    assert hasattr(k2,'zdrowie2') # jesli cos sie nie zgadza to wyrzuca blad , czyli jak nie chcemy, zeby coś mialo taka wartosc to sprawdzmy assertem
except:
    print("k2 nie ma elementu zdrowie2")