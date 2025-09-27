# Understanding Functions in Python
def greet(name):
  """Prints a greeting message."""
  print(f"Hello, {name}!")

add = lambda x, y: x - y
result = add(5, 3)  
print(result)  # Output: 8

# Function Parameters and Return Values
def calculate_area (length, width):
  """Calculates the area of the rectangle"""
  area = length * width
  return area
 
 # argument passing

calculate_area (5, 4)