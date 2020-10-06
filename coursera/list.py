
list21 = ['red',23.2,2]
for l in list21:
    print("Happy New Year: ",l)

friends = ["Joseph","Glenn","Sally"]

for i in range(len(friends)):
    friend = friends[i]
    print("Feliz cumpleanos",friend)

list2 = [1,3,4,32]
list1 = [212,11,8]
l1 = list2 + list1
print(l1)
print(l1[:4])

stuff = list()
stuff.append("book")
stuff.append(81)
print(stuff)

stuff1 = list(range(0,101,10))
print(stuff1)
del stuff1[4]
print(stuff1)
stuff1.insert(2,110)
print(stuff1)

stuff1.insert(5,-123)
stuff1.sort()
print("sorted ",stuff1)
print("len(stuff1)",len(stuff1))
print("max(stuff1)",max(stuff1))
print("min(stuff1)",min(stuff1))
print("sum(stuff1)",sum(stuff1))

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    try:
        value = float(inp)
    except:
        print("Wrong data try again")
        continue
    numlist.append(value)

avg = sum(numlist)/len(numlist)
print("avg is ",avg)

abc = "With three words"
splicik = abc.split()
print(splicik)
for i in splicik:
    i = i.lower()
    if i.startswith("w"): print(i)

line = "first;second;third"
thing = line.split()
print(thing)

thing = line.split(";")
print(thing)


filepath = input("Enter file name: ")
try:
    openfile = open(filepath,'r')
except:
    print("Wrong file path",filepath)
    quit()

for line in openfile:
    if line.startswith("From"):
        line = line.rstrip()
        print(line)
        splitted = line.split()
        email = splitted[1]
        postfix = email.split("@")
        print(postfix[1])


