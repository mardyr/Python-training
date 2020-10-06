a = []
b = [1,2,3]
c = list(['a','b',1,2,44])

print(f" a to {a}, b to {b} , c to {c}")

f = [1,2]
g = [0,5]
h = [0,0]

print(all(h))
print(any(g))

i = [3,2,1,2,4,2,4,2,1,111,432,12,55]
j = [1,4,2,5,99,119,33,12,43,23,53,24,76]
y = sorted(j)
print(len(i))
print(sum(i))
print(i.index(111))
print(i.count(2))

# kopiowanie list
k = j.copy()
k.append(-1)
print(f'k to {k} i j to {j}')
k.extend([2,3,4])
k.insert(3,9)
print(f'k to {k} i j to {j}')
o = k.pop(5)
print("sciganalem cos",o)
k.remove(5)
print(k)
print("3 element",k[3])
k[3] =22
print("3 element",k[3])

k = tuple(k)
k+= ([3,2,1],)
k[-1][2] +=10
print(k)

w= x,*o,z,c = k
print(f"to jest {w}")
print(f"x:{x},z: {z},c = {c}")