a = ()
b = (1,2,3)
c = tuple()
d = (1,)
e = 7,8,9

f = 1,2
g = 0,5
h = 0,0
z = None,3

print(any(f)) # jesli minimum jeden element jest prawda , czyli nie jest zerem i None
print(any(h))

print(all(f)) # wszystkie elementy muszą zwracać true
print(all(z))

print(reversed(b))
print(tuple(reversed(b)))
print(sorted(b))
a = sorted(b)
print(f"to jest a {a}")
b += (1,2)
b = list(b)
b.append(3)
print(f"b: {b}")

k,l = (3,7)

(l,k) = (k,l)
print(f"k:{k},l:{l}")

e = 7,8,9
print(len(e))
print(sum(e))

j = 3,2,1,4,5,7,9,7,8,4,2,5,4
print(j.index(9))
print("Ile jest 7 ",j.count(7))

print(j[:5])
print(j[-1])
print(j[::2]) # co drugi element
print(j[2::3]) # od 3 elementy(bo od 0) co 3 elementy
print(j[8::-2])

c = j
print(c)

c = k,z,*x,l = j
print(f"k to {k} i l to {l} i {z}")

b = 3,8,9

*r,x = b
print(f"r to {r}")

