'''
count = {}
data = input("Enter data: ")
data = data.split()
for word in data:
    count[word] = count.get(word, 0)+1

print(count)

'''
file_name = input("Podaj nazwe pliku: ")
if len(file_name) < 1 : file_name = 'clown.txt'
with open(file_name) as file:
    counter = dict()

    for line in file:
        line = line.rstrip()
        spliter = line.split()
        for word in spliter:
            counter[word] = counter.get(word, 0) + 1

    lst = sorted([(v, k) for k, v in counter.items()])



    for val, key in lst[:5]:
        print(key, val)

    #*********************************************************************
    print(sorted(counter.items()))
    highestValue = None
    key = None
    for k, v in counter.items():
        if highestValue == None or v > highestValue:
            highestValue = v
            key = k

    print(key,highestValue)

c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v, k))

print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)