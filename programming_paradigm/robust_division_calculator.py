def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for invalid inputs and division by zero.
    Returns a string message with the result or an error.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
