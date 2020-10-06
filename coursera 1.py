'''
eee = "hello" + " there"
print(eee)
eee = eee + " "+ str(5)
print(eee," ",type(eee))

print(float(99)+100)
i = 42
print(type(i))
import math as m
print(m.floor(10.6))

print(9//2)

sval = '123'
ival = int(sval)
print(ival+1)

name = input("What's your name")
print("Welcome", name)
'''
# Converting User Elevator input
'''
inp = input("Set elevator floor ")
number = int(inp) +1 # conversion to US floor
if number <1 :
    print("WRONG NUMBER OF FLOOR ")
else:
    print("We are on",number,'floor in USA')

x = int(98.6)
print(x)
'''
# Condtional Patterns
'''
x = 5

if x<4:
    print("LESS THAN 4")
else:
    print("Greater or equal 4")
print("END OF IF STATEMENT")

n = input("Enter number ")
try:
    x =n + 1
    print(x)
except :
    print("WELCOME IN EXCEPT PART")
'''

x = 5
print('Hello')

def print_sth() :
    print("I'm driving in a highway in my volkswagen Beetle")
    print('''I love you baby
I love you baby''')

print('x =',x+3)
print_sth()

def greet(lang) :
    if lang == 'es':
        return 'Hola'
    if lang == 'fr':
        return 'Bonjour'
    if lang == 'en':
        return 'Hello'

print(greet('es'),'Michael')

'''
while True:
    line = input('>')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
'''
'''
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff')

friends = ['Joseph','Glenn','Sally']
for friend in friends :
    print('Happy New Year:',friend)
print('Done!')
'''
zork = 0
print('Before',zork)
for thing in [23,11,3,32,8,9]:
    print(thing, zork)
    zork+=thing
    print("Suma",zork)
print('After',zork)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        number = int(num)
    except:
        if num!="done":
            print("Invalid input")
            continue
    if largest is None :
        largest = number
        smallest = number
    elif number < smallest :
        smallest = number
    elif number > largest :
        largest = number
    elif num == "done": break


print("Maximum", largest)
print("Minimum", smallest)