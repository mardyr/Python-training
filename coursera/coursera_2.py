str1 = "Hello"
str2 = "World"
bob = str1 + " Heeey " + str2
print(bob)
'''
index = 0
while(index<len(bob)):
   char = bob[index]
   print("[",index,"]",char)
   index = index +1
 '''
for i in bob:
    print(i)



str3 = "123"
res = str3 + str(7)
print("First letter",res[0])
print("Last letter",res[len(res)-1])

wyn = int(str3) + 1
print(wyn)

wynik = input("Enter int: ")
print(type(wynik))

word = "banana"
count = 0
for i in word :
    print(i)
    if i == "a" : count+=1

print("count value",count)

string = "Monthy Python"
print(string[4:20])

print(string[8:]) # od 8 znaku do konca

