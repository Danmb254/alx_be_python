# Inheritance
"""class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Wolf!")

lassie= Dog("Lassie")
lassie.make_sound()"""

"""class Flyer:
    def fly(self):
        print("Flying")
class Swimmer:
    def swimm(self):
        print("Swimming")
class Duck(Flyer,Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swimm()"""

class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(C or B):
    pass

# Creating an instance of class D
obj_d = D()
print(obj_d.greet()) 