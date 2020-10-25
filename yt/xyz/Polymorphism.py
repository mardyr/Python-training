class Shape:
    def __init__(self, name = 'Shape'):
        self.name = name

    def area(self):
        print("No data about ", self.name)

class Triangle(Shape):

    def __init__(self, name='Triangle', edge=2, height=2):
        super().__init__(name)
        self.edge = edge
        self.height = height

    def area(self):
        print("Area of", self.name)
        print((self.edge*self.height)/2)

class Rectangle(Shape):

    def __init__(self, name='Rectangle', a=2, b=2):
        super().__init__(name)
        self.a = a
        self.b = b

    def area(self):
        print("Area of", self.name)
        print(self.a*self.b)

class Square():

    def __init__(self, name="Square",a=2):
        self.name = name
        self.a = a
    def area(self):
        print("Area of ", self.name)
        print(self.a**2)

def show_area(list):
    for element in list:
        print(type(element))
        element.area()
        print(60 * '*')

shape = Shape("Myshape")
triangle = Triangle("Mytriangle",3)
rectangle = Rectangle("Myrectangle",3,4)
square = Square("Mysquare",1)


shape_list = [shape,triangle,rectangle,square]

show_area(shape_list)
