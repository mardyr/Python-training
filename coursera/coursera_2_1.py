string = "Hello It's me"
zap = string.lower()
print("Capitalize ",zap.capitalize())

print(zap)
print(string)

#find operator , returning position

fruit = "banana"
up = fruit.upper()
low = fruit.lower()

pos = fruit.find("na")
print(pos)

expr = "Hello Martin"
nstr = expr.replace('l','x')
print(nstr)
xstr = expr.replace("Martin","John")
print(xstr)

word = "   I like fun  "
print(word.lstrip()) # "I like fun  "
print(word.rstrip()) # "   I like fun"
print(word.strip()) # "I like fun"

print(word.startswith('I')) # od czego zaczyna sie wyrazenie


data = "From marcindyrdol@gmail.com Sat Agt 6 12:18:12 2020"

pos = data.find("@")
print(pos)

endpos = data.find(" ",pos); # odkad zaczynam szukac

host = data[pos+1:endpos]
print(host)

str = "X-DSPAM-Confidence: 0.8475"
begin = str.find(" ")
print(begin)

res = str[begin+1:]
print(res)
value = float(res)
print(type(value))