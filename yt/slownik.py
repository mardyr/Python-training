keywords = ('imie','nazwisko','miasto')
a = 0

# tworzenie slownikow

x = {}
y = {'a':3,'b':'domek','c':2}
z = {}.fromkeys(keywords,a)
m = dict()
print(f'x: {x}, y: {y}, z: {z},m: {m}')

x['a'] = 1
y.update({'a':2})
z.update(x)
e = z.setdefault('R',2)
print(f'x: {x}, y: {y}, z: {z}, e: {e}')

print(x['a'])
print(x.get('a'))

for k,v in y.items():
    print(f"Hey ho {k} i mamy {v}")

# kopiowanie

q = z.copy()
w = z
z.setdefault('x',2)
print(f'w to {w} , z to {z} , q to {q}')
z.popitem()
print("z iii", z)
# kasowanie
x = {}
w.clear()
print(f"x : {x}, w: {w}")

print(f'y: {y}')
y.pop('a')
print(f'y: {y}')

