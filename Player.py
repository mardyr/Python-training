class Player:
    def __init__(self, name = "Noname", age = 0, height = 0.0):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return f"Player {self.name}, {self.age} age , {self.height:.2f}"

class Goalkeeper(Player):
    '''klasa bramkarz'''
    def __init__(self,name,age,height,arm_distance,strength):
        super().__init__(name, age, height)
        self.arm_distance = arm_distance
        self.strength = strength
    def __str__(self):
        return super().__str__() + f" arm distance equal{self.arm_distance}, strength equal {self.strength}"

p = Player('Marcin',10,1.789)
print(p)
g = Goalkeeper("Dida",33,1.92,1.03,70)
print(g)
print(g.__class__)
print(g.__doc__)
print(Goalkeeper.__doc__)
print(Goalkeeper.mro())

print(hasattr(g, 'name'))
print(getattr(g,'age',-99))

try:
    assert hasattr(g,'cash')
except AssertionError as msg:
    print(msg)
