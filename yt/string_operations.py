text = "Dziwny jest ten świat\t gdzie jeszcze wciaz 123232"

print(text.capitalize())

print(text.center(70,'*'))

print("CASEFOLD",text.casefold())

print(text.count('i',35,40))

print(text.startswith("Dziwny"))
print(text.endswith("jest"))

print(text.startswith(("gdzie","ten","Dziwny"))) # tuple , jedno z nich musi wystapic

print(text[0:15])

print(text.endswith(("gdzie", "miesci","ten"),0,15))

print(text.expandtabs(2))  # zmiana wielkosci tabulacji na 2 spacje , chyba z 4

print(text.encode('ascii','ignore'))

print(text.encode('ascii','replace'))

print(text.encode('ascii','backslashreplace'))

pos = text.find("i",4,8)

if pos>0: print(text[pos:])

try:
    inpos = text.index("i",4,8)
except Exception as e:
    print("TO JEST exception",e)

print(text[-6:])
# 3 metody na sprawdzenie czy ciąg znaków jest zlozony tylko z liczb
print(text[-6:].isnumeric())

print(text[-6:].isdecimal())

print(text[-6:].isdigit())

# Sprawdzenie czy ciag znakow zlozony jest z liter

print(text[:6])
print(text[:6].isalpha())

text_alnum = "abc123"
text_alnum.isalnum() # return true if chain of signs is literals or digits

text_ascii = text.encode('ascii','ignore') # ignoruje wszystko co nie jest ascii
print(text_ascii.isascii())

text_lower = text.lower()
print(text_lower)
print(text_lower.islower())

text_upper = text.upper()
print(text_upper.swapcase()) # zamiana na male litery

text_space = " "
print("Jest spacją? ", text_space.isspace())

text_title = "Hello world"
text_title = text_title.title()
print(text_title)
print('..'.join(['król','dama','walet']))

print('abc'.ljust(10,'x'))
print('abc'.rjust(10,'*')) # justowanie do prawej
print('-48'.zfill(5))
print('-48'.rjust(5,'0'))

"   *Python jest super".lstrip()
print("   *Python jest super".lstrip("* ")) # usuwa od lewej strony te znaki ktore podamy
print("   *Python jest super".rstrip("repsutj "))
print("  *Python jest super".strip("*repsutj "))

t = "tekst,do,pociecia,ale to dziwne"

print(t.split(','))

print('python to zło'.replace("to zło","jest super"))


