#building classes with python
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"The {person1.name} and {person2.name} information will be deleted")
person1 = Person("Daniel", 12)
person2 = Person("Pato", 24)

print(f"My name is {person1.name} is {person1.age}")
print(f"My name is {person2.name} is {person2.age}")"""

class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created for {self.name}, age {self.age}.")

    # Destructor to print a farewell message
    def __del__(self):
        print(f"Goodbye {self.name}, your object is being deleted.")

# Example usage
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Deleting one object explicitly
del person1


