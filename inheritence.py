
class Ryba():
    def __init__(self,imie="Nemo",wiek=0):
        self.imie = imie
        self.wiek = wiek
    def __str__(self):
        return f"Imie ryby to {self.imie}, a wiek {self.wiek}"
    def wyswietl (self):
        print("Jestem ", self.imie, " i mam ", self.wiek , " lat. ")

class Tunczyk(Ryba):
    def __init__(self,imie="Roro",wiek=11):
        super().__init__(imie,wiek)
    def __str__(self):
        super().__str__()



fish = Ryba("Fishyy",12)
print(fish)
tuna = Tunczyk()
tuna.wyswietl()


