cars = list(["bmw","mercedes","audi","fiat","toyota","nissan"])

print(cars[::-1])
print(cars[2::-1]) # czyli od 2 do konca z krokiem -1

cars.append("Jeep")
cars.extend(["rover","honda"])
print(cars)
cars+= ["suzuki","opel"]
print(cars)

cars.remove("audi")

try:
    cars.remove("audi")
except:
    print("UUUUJ")

################

fruits = ["banana","raspberry","apple","banana"]

print(fruits.index("banana"))
print(fruits.index("banana",1,len(fruits)))

print(sorted(fruits)) ## sortowanie na kopii
print(fruits)
fruits.sort(key=len)
print("sortowanie na dlugosc ")
print(fruits)

nums = [1,6,7,3,5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
