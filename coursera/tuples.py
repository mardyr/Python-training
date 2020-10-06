x = tuple()
x = x + (1,)
x = x+ (1,2,4,112,"Halo")
print(x)

def myFunc(e):
    return len(e)

cars = ["Ford","Mitsubishi","BMW","VW"]

cars.sort(key=myFunc)
print(cars)


num = [1,343,-1,223,12]
num.sort()
print(num)

res = (0,1,2) <(0,1,3)
print(res)
r = ("joan","Ron","Son") < ("Joe","Moer","Toe")
print(r)



d = {"b" : 11 ,"a" : 8,"d" : 34,"c" : 12}
print(d)
a = sorted(d.items())
print(a)

for k,v in sorted(d.items()):
    print(k,v)

c = {"a":10,"b":1 ,"c":22}
tmp = list()
print(c)
for k,v in c.items():
    print(k,v)
    tmp.append((v,k))

print(tmp)
tmp.sort(reverse=True)
# tmp = sorted(tmp,reverse=True)
print(tmp)

path = input("Input file name: ")
try:
    file = open(path,'r')
except:
    print("Can not open file, wrong path or directory")
    quit(1)
wordict = dict()
for line in file: # iterate line by line
    line.rstrip()
    divideline = line.split()
    for word in divideline: # iterate by list
        wordict[word] = wordict.get(word,0)+1

tmp = [] # temporary list
for k,v in wordict.items():
    tmp.append((v,k))

tmp.sort(reverse=True)

for k,v in tmp[:10]:
    print(k,v)

##################################
print(wordict)
c = {"a":10,"c":9,"e":123,"f":1}
print(sorted([(v,k) for k,v in c.items()],reverse=True))
##################################