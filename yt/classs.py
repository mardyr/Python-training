class FirstClass:
    #first_number=0
    #second_number = 0
    '''
    def __init__(self,first_number,second_number):
        self.first_number = first_number
        self.second_number = second_number
    '''

    def __init__(self, first_number=10, second_number=22):
        self.first_number = first_number
        self.second_number = second_number
    '''
    def __init__(self, *args):
        self.first_number = args[0]
        self.second_number = args[1]
    '''
    def __str__(self):
        return f'Jestem obiektem klasy {self.__class__.__name__}'

    def sum(self):
        return self.first_number+self.second_number

object_first_class = FirstClass(12,2)

print(object_first_class)
print(type(object_first_class))

object_first_class.first_number = 123
object_first_class.third_number = 11
print(object_first_class.third_number)

print(object_first_class.sum())
print(object_first_class.__dict__)

print(object_first_class.__dir__())


class SecondClass(FirstClass):


    def __init__(self):
        super().__init__()
        self.third_number = 87


object_second_class = SecondClass()

#print(object_second_class.first_number,object_second_class.second_number)

print(object_second_class.__dict__)
