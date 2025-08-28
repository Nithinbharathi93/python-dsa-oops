class Animal:
    def __init__(self, name):
        self.name = name

class Prey(Animal):
    def flee(self):
        print(f"{self.name} will flee")
    def action(self):
        print("I run")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} will hunt")
    def action(self):
        print("I chase")

class Rabbit(Prey):
    pass 

class Hawk(Predator):
    pass 

class Fish(Prey, Predator):
    pass 

fish = Fish("Nemo")
fish.flee()
fish.hunt()
fish.action()