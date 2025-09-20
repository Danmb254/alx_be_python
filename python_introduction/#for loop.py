#for loop
fruits = ["apple", "bananas", "oranges"]
for fruit in fruits:
    print(fruit)

#for tuples
colors = ("blue", "green", "red")
for color in colors:
    print(color)

# Looping Through Characters in a String

message = "Hello, world!"

for character in message:
  print(character)   

successful = False
for numbers in range (3):
    print ("Attempt")
    if successful:
        print("This was successful")
        break
else:
    print("Attempted 3 times and failed")

#exercise 
numbers = [1, 5, 3, 9]
for total in numbers:
    print(total)

# while
age = 0

while age >= 18:
    age = int(input("What is your age(omly  18 and above can proceed):"))
print("You're old enough to proceed.")