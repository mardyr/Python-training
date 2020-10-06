
class Calculator():

    # metody magiczne __nazwa__
    def __init__(self):   #konstruktor
        print("Init")
    def __del__(self):
        print("Delete object") #destruktor

    ## tutaj takie przeciazenia operatorow
    def __str__(self):
        return "Hello"
    def __int__(self):
        return 10
    def __len__(self):
        return 5
    def __bool__(self):
        return True
    ####################################
    def dodaj(self,a,b):
        wynik = a+b
        print(wynik)
    def odejmij(self,a,b):
        wynika = a-b
        print(wynika)


calcinstance = Calculator()

calcinstance.dodaj(2,4)
print(calcinstance)

if calcinstance:
    print("Calc exists")
else
    print("calc not exists")


def main():
    calc = Calculator()
    print("Dodawanko")
    calc.dodaj(3,2)
    calc_2 = Calculator()
    #calc_2.dodaj(32,8)

