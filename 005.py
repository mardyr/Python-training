zbior = {1,2,2,3} # zbior to taka lista tylko, ze nie moga byc powtarzajace sie elementy
print('zbior= ',zbior,type(zbior)) # 1 2 3
zbiór2 = {} # pusty słownik
print("zbiór ",zbiór2,type(zbiór2))

zbiór3 = set()
print(zbiór3,type(zbiór3))
zbiór3.add(1)
zbiór3.add(3)
zbiór3.add(100)
zbiór3.add(0)
zbiór3.add(100)
zbiór3.add(4)
print('zbiór3',zbiór3,type(zbiór3))
zbiór3.remove(100) # element musi istniec
zbiór3.discard(2) # usuwa element,ale element nie musi istniec
print("zbiór 3 ",zbiór3)
print("poop",zbiór3.pop())

print("zbiór 3 ",zbiór3)
zbiór3.discard(3)
print(zbiór3)
zbiór3.clear()

set1 = set([5,4,1,2,3,3,3])
print("set1",set1)

set2 = set("literki")
print("set2",set2)
set3 = sorted(set2)
print("sorted set 2",set3)

set4 = set([3,4,5,6,7,8])
print(set1.difference(set4)) # to co jest w set1 ale nie ma w set4
print(set1.union(set4)) # polaczenie zbiorow
print(set1.intersection(set4)) # czesc wspolna
print(set1.isdisjoint(set4)) # true jak nie ma wspolnych elementow
print(set1.issubset(set4)) # true jak set1 zawrze sie w set4 w calosci
print(set1.issuperset(set4)) # true jak kazdy z set4 jest w set1
set5 = set4.copy()
print(set5)

# słownik

słownik = {"a":34,"berd":"x",12:"elo",13:3.4}
print("słownik",słownik[13],type(słownik))
print(słownik["berd"],słownik["a"], słownik[12],sep=" * ")
del słownik['a']
print(słownik)

di = dict() # pusty słownik
di['woda'] = 'gazowana'
di['piwo'] = 'chmielowe'
di['procent'] = 5.2
di['wino'] = 'półsłodkie'
print(di)

di2 = di.copy()
print("Kopia",di2)
di2.clear()
print(di2)
print('Długość',len(di))
print(di['woda']) # tutaj musimy byc pewni czy istnieje , jak remove
print(di.get('wino',' nie ma win')) # tutaj takie zabezpieczenie
print('woda'in di)
print('wod' in di)
print(di.items())
print(di.keys())
print(di.values())
print(di.popitem()) # usuwa ostatni dodany element , czyli wino - półsłodkie
print(di)
print(di.update(procent='4'))
print(di)