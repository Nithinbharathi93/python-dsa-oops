class Animal:
    def __init__(self, name):
        self.name = name 
        self.is_alive = True 
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Bark Bark")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

class Mouse(Animal):
    def speak(self):
        print("Squek squek")

dog = Dog("mani")
cat = Cat("tom")
mouse = Mouse("eli")

print(mouse.name)
mouse.eat()
mouse.speak()