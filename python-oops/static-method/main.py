class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is the {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["dev", "manager", "tester", "ba"]
        return position in valid_positions
    
emp1 = Employee("Nithin", "Sr Dev")
emp2 = Employee("Mick", "Trianee")
    
print(Employee.is_valid_position("Janitor"))

print(emp1.get_info())
print(emp2.get_info())