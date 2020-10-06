
myDict = {
    "Lewis Hamilton" : 44,
    "Sebastian Vettel" : 5,
    "Carlos Sainz" : 55,
    "Daniel Riccardo" : 3,
}

# dodawanie elementow

myDict["Lando Norris"] = 4

driv = myDict.pop("Carlos Sainz",-5)
print(driv)
print("drivv")


driver_name = "Nico Hulkenberg"
driver = myDict.get(driver_name,0)
print(driver)

print(myDict["Lewis Hamilton"])
klucze = list(myDict)
print(klucze)
print(len(myDict))
print(myDict)

del myDict["Lewis Hamilton"]

for k,v in myDict.items():
    print(f'k to {k} i  val to {v}')