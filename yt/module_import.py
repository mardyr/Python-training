from foo import test,suma as s
from time import time

def suma(x,y):
    return x*y


print(suma(2,8))


timer = time()
timer2 = time()
while True:
    if(time() - timer > 2):
        test("Hello")
        test("My way")
        timer = time()
    if(time() - timer2 >10): break

print(s(2,8))