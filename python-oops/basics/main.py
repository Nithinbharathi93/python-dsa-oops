from car import Car 

# Creating an object
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Maruthi", 2025, "black", True)
# print(car1.model)
print(car1.year)
print(car2.year)
# print(car1.color)
# print(car1.for_sale)

car1.drive()
car2.stop()