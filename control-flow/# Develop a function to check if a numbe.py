# Develop a function to check if a number is even or odd.

def check_number_odd_even(number):
    """Check a number is odd or even"""
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
check_number_odd_even(8)