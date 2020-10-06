
class Calculator():

    def __init__(self):
        print("Construct object")
        self.ostatni_wynik=0
    def __del__(self):
        print("Destruct object")


    def suma(self,x=1,y=12):
        wynik = x+y
        self.ostatni_wynik +=wynik
       

    def odejmij(self,x,y):
        wynik = x-y
        self.ostatni_wynik-=wynik


calc = Calculator()

calc.suma(3,8)

print("Ostatni wynik {}".format(calc.ostatni_wynik))

calc.odejmij(2,1)
print("Ostatni wynik {}".format(calc.ostatni_wynik))