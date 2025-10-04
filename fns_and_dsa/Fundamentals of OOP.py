
"""class Car:
    def __init__(self, model, color, year ):
        self.model = model
        self.color = color
        self.year = year
    
    def display_info(self):
        return f"{self.year}, {self.model}, {self.}"


# Create objects using __init__
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)
car3 = Car("Range", "autobio", 2024)

print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2023 Tesla Model 3
print(car3.display_info())"""

#exercise 1:Define a Student class with attributes like name and age. Include a method to display student information.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_information(self):
        return f"{self.name} {self.age}"
    
Student1 = Student("Daniel", 28)
Student2 = Student("Pato", 25)
Student3 = Student("Moh", 23)

print(Student1.student_information())
print(Student2.student_information())
print(Student3.student_information())




    