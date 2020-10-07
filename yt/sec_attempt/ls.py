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

sum1 = 0
total_time = ('Lewis Hamilton', 78.89, 79.89, 78.99, 80.89, 80.84)
print(total_time[0])
sum1 = sum(total_time[1:])

print(sum1)
t = (1, 2, 3, 4, )
t+= (5, 6, )
print(t)