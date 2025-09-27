def greet(name="World"):
     """Prints a greeting message."""
     print(f"Hello, {name}!")
greet() 
greet ("Daniel")
greet ("pato")

# return fuction
def square (number):
     """prints the square of a number"""
     return number * number
print(square(4))

count = 0  # Global variable
def increment():
     count += 1  # This refers to the local count within the function
    
print(count)  # Output: 0 (Global count remains unchanged)

count = 0
def increment_global():
  global count
  count += 1
increment_global()
print(count)  # Output: 1 (Global count is modified)