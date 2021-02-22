# Python Arrays
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print()

# Access the Elements of an Array
x = cars[1]
print(x)
print()

print(cars)
cars[0] = "Scania"
print(cars)
print()

#The Length of an Array
lenArray = len(cars)
print(lenArray)
print()

# Looping Array Elements
for c in cars:
    print(c)

# Adding Array Elements
cars.append("Innoson")
cars.append("Toyota")
print(cars)
print()

# Removing Array Elements
cars.pop(2)
print(cars)
print()

cars.append("Tesla")
cars.append("Volkswagon")
print(cars)
print()

cars.remove("Volvo")
print(cars)
print()

cars.sort()
print(cars)
print()