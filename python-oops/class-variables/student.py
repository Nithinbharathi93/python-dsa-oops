class Student:

    college = "SNS College of Technology"
    number_of_student = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 
        Student.number_of_student += 1
    
st1 = Student("nithin", "final-year")
st2 = Student("Pat", "pre-final-year")
st2 = Student("Sandy", "second-year")

print(st1.name)
print(st2.grade)

print(st1.college)
print(st2.college)

print(st1.number_of_student)
print(Student.number_of_student)
