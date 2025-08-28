class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position 
        
        def get_details(self):
            return f"{self.name} is a {self.position}"

    def __init__(self, company_name):
        self.company_nam = company_name
        self.employee = []
    
    def add_employee(self, name, position):
        new_emp = self.Employee(name, position)
        self.employee.append(new_emp)

    def list_employee(self):
        return [emp.get_details() for emp in self.employee]

company = Company("Google")

company.add_employee("Sundar", "CEO")
company.add_employee("Nithin", "Jr.Dev")

print(*company.list_employee(), sep="\n")