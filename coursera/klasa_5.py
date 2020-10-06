class Human:

    def __init__(self,wiek,imie,wzrost,narodowosc="Polska"):
        self.wiek = wiek
        self.imie = imie
        self.wzrost = wzrost
        self.narodowosc = narodowosc
        self.__pesel = 00000000000
    def __del__(self):
        print("Destruktor")
    def __str__(self):
        return "[{1},{0} : {2} ;;{3}".format(self.wiek,self.imie,self.wzrost,self.narodowosc)
    def mojaMetoda(self):
        print(self.imie+" "+self.nazwisko)

c1 = Human(20,"Marcin","Dyrdol",1.90)
c1._Human__pesel = 89381331391
print(c1._Human__pesel)
print(c1)

formated_text = f"{c1.wzrost} {c1.imie} {c1.narodowosc} to takie podstawowe dane"
print(formated_text)