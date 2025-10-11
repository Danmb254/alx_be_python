class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: works independently of any class or instance data"""
        return a + b
    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to the class itself through 'cls"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
