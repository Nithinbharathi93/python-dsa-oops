from abc import ABC, abstractmethod # ABC - Abstract Base Class
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Drive the car")

    def stop(self):
        print("Stop..! Stop the Car")

class Moto(Vehicle):
    def go(self):
        print("Drive the bike")
        
    def stop(self):
        print("Stop..! Stop the Bike")

class RE(Moto):
    def go(self):
        print("Com'on baby let's go on the Bullet-uh")

v1 = Car()
v1.go()
v1.stop()

vandi = RE()
vandi.go()