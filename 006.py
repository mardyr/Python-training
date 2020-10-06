import time

tup = (1,3,5)
if 1 in tup:
    print("IF1")
    print(type(tup))
    time.sleep(5)

if 4 in tup or True : print("IF2"); print(type(tup)); time.sleep(5)

it = 'kura'
print("IF ELSE")
if it[1] =='u':
    print("inside")
    print(len(it))
    pass # pusta instrukcja
else:
    print("outside")

if False:
    pass
elif 1>0:
    print("elif - elf czy to nie elf?"); pass
else:
    pass

efect = 5 if 'r' in 'kura' else 10
print("efekt= ",efect)
efect2 = -1 if 'z' in 'kura' else -2 if False else -3 # efect2 = -1 if 'z' in 'kura' else (-2 if False else -3)
print('efect2= ',efect2)

kotlety = [1,2,3,4,5]
while len(kotlety):
    print("Zjedzony kotlet nr",kotlety.pop())

x = 11
while x>0:
    x-=1 # x= x-1
    if x==4 :
        break
    elif x==7 :
        continue
    else :
        print(x)

for x in range(1,4):
    print(x)

for literka in 'jakieś słowo':
    print(literka,end=" ")
print("\n")

słownik = {'a':1,'b':2,'c':3}
for x in słownik:
    print(x,'',słownik[x])