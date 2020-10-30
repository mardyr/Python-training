#iterator to obiekt który sluzy do przegladania elementow kolekcji


list = [1,3,4]

list_iterator = iter(list)
print(list_iterator)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))


class MyIterator():
    def __init__(self,data = "Napis"):
        self.data= data
        self.indeks = len(data)

    def __iter__(self):
         return self
    def __next__(self):
        if self.indeks == 0 :
            raise StopIteration
        self.indeks-=1
        return self.data[self.indeks]

for i in MyIterator("Marcin"):
    print(i,end = "")

print()
for i in MyIterator([1,3,5,6,7]):
    print(i,end="")