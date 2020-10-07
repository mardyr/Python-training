from functools import reduce

#-------------------------------------------
# MAP
list_one = [1,1,1,1,1,1,1]
def multiply(m):
    return m*22
print(list_one)
print(list(map(multiply,list_one)))
print(list(map(lambda x: x*3, [3, 2, 5, 8, 3, 2])))
#--------------------------------------------------
# FILTER
my_list = [1, 2, 4, 7, 6, 15, 34, 77]
def is_odd(x):
    if x%2 == 1:
        return x
print(my_list)
print(list(filter(is_odd,my_list)))

#--------------------------------------------------
# reduce , import from functools , zwraca wynik, taka suma kroczaca

reduce_list = [11,3,4,6,9,44,22,25]
def dodaj(a,b):
    return a+b
print(reduce(dodaj,reduce_list))

#--------------------------

funLambda3 = lambda x : 'Tak' if x % 2 == 0 else 'Nie'
print(funLambda3(5))

print(list(map(lambda x: 'Tak' if x % 2 == 0 else 'Nie',[3,2,5,8,2])))

print(list(filter(lambda x: x % 2 == 0, [5, 2, 5, 7, 6, 8, 12])))

