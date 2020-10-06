fileopen =  input("Enter file path: ")
if len(fileopen) < 1 : fileopen = "gould.txt"
file = open(fileopen,'r')
di = dict()
for line in file:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        #print("**",w,di.get(w,-99))

        di[w] = di.get(w,0)+1
print(di)
print(wds)
for key in di:
    if di[key] is max(di.values()) : print(key,di[key])

max = None
key = None
for a,b in di.items():
    if max is None or b>max:
        max = b
        key = a
print(key,max)
