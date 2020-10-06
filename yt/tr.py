keywords = ("x","y","z","l","e")
b = 2
x = {}.fromkeys(keywords,b)
print(x)
z = {}
y = {'x':23,'y':1,'z':12}
print(y)

m = dict()

m.update({"a":2})
m.update({"b":17})
m.update({"c":1})
m.update({"d":23})
m.setdefault('d',44)
print(f"m = {m}")
