'''
purse = dict()
purse["money"] = 13
purse["candy"] = 4
purse["tissues"] = 75
print(purse)

purse["candy"] += 121
print(purse)

jj = {'chuck' : 1,'fred' : 42, 'jan' : 100}
print(jj)

jj["jan"] = -1
print(jj)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['csev']+=1
print(ccc)

count = dict()
names = ["csev","cwen","zqian","csev","cwen"]

for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
print(count)

counter = dict()
namex = ["csev","cwen","zqian","csev","cwen"]

for n in namex:
    counter[n] = counter.get(n,0) + 1

print(counter)
'''
count = dict()
filepath = input("Enter file name: ")
try:
    file = open(filepath,'r')
except:
    print("Wrong filepath")
    quit()
for line in file:
    line = line.rstrip()
    linedivide = line.split();
    for i in linedivide:
        count[i] = count.get(i,0) + 1

# for key in count:
   # if count[key] is max(count.values()): print(key,count[key])
key = None
max = None
for a,b in count.items():
    if max is None or b > max:
        key = a
        max = b


print(key,max)