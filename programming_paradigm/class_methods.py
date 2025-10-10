class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1 # Increment count on instance creation
    @classmethod
    def display_count(cls):
        print(f"The total number of persons: {cls.count}")

person1 = Person("Daniel")
person2 = Person("Moreen")
Person.display_count()

        