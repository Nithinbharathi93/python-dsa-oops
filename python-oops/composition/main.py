class Engine:
    def __init__(self, hp):
        self.hp = hp

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, hp, wheel_size):
        self.make = make
        self.model = model 
        self.engine = Engine(hp)
        self.wheels = [Wheel(wheel_size) for i in range(4)]
    
    def display(self):
        return f"{self.make} {self.model}"

car = Car("Tata", "Nexon", 500, 18)

print(car.display())