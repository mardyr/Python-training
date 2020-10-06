

lista = list(range(10))

nowa = [i * 2 for i in lista]
print(lista)
print(nowa)
nowa2 = [i + 1 for i in lista if i % 2 == 0]
print(nowa2)



print(", ".join(["a","b","c"]))
print("Hello World".replace("Hello","Bye"))
print("OOLOLOLO".startswith("xy"))
print("OOLOLOLO".endswith("O"))
print("To jest zdanie".upper())
print("To jest zdanie".split())

lista = [10,20,30,40,45,55,60]

for i,element in enumerate(lista):
    print(f"[{i}] {element}")


