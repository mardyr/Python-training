import math
class MyVector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Współrzędne to {self.x} i {self.y}"
# chcemy zeby dziala +
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)
# chcemy zeby dla naszych obiektow dzialal +=
    def __isadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self
    def length(self):
        return int(math.sqrt(self.x**2 + self.y**2))
vec1 = MyVector()
vec2 = MyVector(2.1 , 4.2)
vec3 = vec1 + vec2
vec3 += vec2

print("Wektor 1 ", vec1,f" o długości {vec1.length()}")
print("Wektor 2 " , vec2,f" o długości {vec2.length()}")