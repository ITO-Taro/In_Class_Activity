# 1. In this file I want you to create a Dictionary named car.
# 2. The car has a brand, a model, and year.
# 3. This dictionary should describe the following object:
# 4. 1964 Ford Mustang
# 5. Access the dictionary to print the value of the “model” of the car.
# 6. Submit your file as an assignment on populi.

car = {"Brand": "Ford", "Model": "Mustang", "Year": 1964}
car1 = dict(Brand = "Ford", Model = "Mustang", Year = "1964")

# print the value of the model by using .get()
print(car.get("Model"))

# value
print(car1.values())

# print values without prentices, hoping for the same result as values()
print(car1.values)

# keys
print(car.keys())

# items
print(car.items())

# setdefault
print(car1.setdefault("Brand"))

# pop
car.pop("Brand")
print(car)

# update
car.update(Model = "GT")

# popitem
car.popitem()
print(car)

