class Car:
    def __init__(self, model, year, color, for_sale): # dunder method - double underscore method
        # self - this object that we are creating right now
        self.model = model 
        self.year = year 
        self.color = color 
        self.for_sale = for_sale 
        # above mentioned are the list of attributes of the Car class
    
    # here comes a method
    # Methods are actions that an object can perform
    def drive(self):
        print(f"you drive the {self.model}")
    def stop(self):
        print(f"you stopped the {self.model}")
    