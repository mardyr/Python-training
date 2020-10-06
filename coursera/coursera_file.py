file = "Hello\nWorld"
print(file)
filename = input("Enter file name: ")
try:
    openfile = open(filename)
except:
    print("File cannot be opened: ", filename)
    quit()
count = 0
for line in openfile:
    line = line.rstrip()
    if not "gmail" in line:
        continue
    begin = line.find(":")
    count+=1
    print("maile: ",line[begin+2:]," z pliku ",filename,"count: ",count)

# wyswietl wszystko co w pliku tekstowym zamieniajac na duze litery

filename = input("Enter file name: ")
try:
    opfile = open(filename)
except:
    print("File cannot be opened ", filename)
    quit()

for line in opfile:
    line = line.rstrip()

    printline = line.upper()
    print(printline)
