t = ("a",)
print(type(t))

t1 = (1,"banana",True)
print(t1)
x,y,z = t1
print(x,y,z)
tx = ("wine","vodka","beer","water","cogniac")

print(tx[::-1])

print(tx[2::-1])

tn = tx + ("tee",)

print(tn)
ntuple = sorted(tn,key=len)
print(ntuple)

a = 3,5,6,2
print(type(a))
*x,z,y = a
print("to x")
print(x)
print(f"z to {z}, a y to {y}")