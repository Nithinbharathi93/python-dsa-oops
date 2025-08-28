from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad 
    def area(self):
        return 3.14*(self.rad**2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    
class Pizza(Circle):
    def __init__(self, toppings, rad):
        super().__init__(rad)
        self.toppings = toppings

shapes = [Circle(7), Square(5), Pizza("pepperoni", 5)]

## Pizza is a Circle and a Shape - Polymorphism..!

for i in shapes:
    print(f"{i.area()} sq cm")