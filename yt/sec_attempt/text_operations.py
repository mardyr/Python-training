
filename = input("Enter file name: ")
try:
    openfile = open(filename)
except:
    print("Cannot open file: "),filename
    quit()

counter = dict()
for line in openfile:
    line = line.rstrip()
    linedivide = line.split();
    for i in linedivide:
        counter[i] = counter.get(i, 0) + 1


key = None
max = None
for a,b in counter.items():
    if max is None or b > max:
        key = a
        max = b


print(key,max)

openfile.close()