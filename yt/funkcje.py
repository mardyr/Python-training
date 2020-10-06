def myFunc(a=3,b=1,c=6):
    if b == 0: pass
    else:  return (a+c)/b


print(myFunc(32,c=11))

def dodaj(a,b=12,c=18):
    return a+b+c

print(dodaj(21))

print(dodaj(11,c=9))


def ileCzego(a,b="default"):
    a = int(a)
    print((b+" ")*a)

ileCzego(3)

ileCzego(4,"*-*")

f=ileCzego

f(3,'*')

napis ="ileCzego"
x=10
tpl = "#"

eval(napis+"("+str(x)+",tpl)")

var = 22
var1 = 11
def changeGlob():
    global var
    var = -3
    var1 =8
    print("scoped var1",var1)
changeGlob()
print("var",var)
print("var1 global",var1)

def multiArgs(*args):
    suma = 0
    for arg in args:
        if(isinstance(arg,int) or isinstance(arg,float)): suma+=arg
    return suma

nums = (1,2,4,5.3,0.5,'rabarbar')

wynik=multiArgs(*nums) # tutaj nums to takie rozpakowanie
print(wynik)