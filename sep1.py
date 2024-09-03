class Calculator:
    def __init__(self):
        # This can be used for initialization if needed
        pass

    def add(self, x, y):
        """Return the sum of x and y."""
        return x + y

    def subtract(self, x, y):
        """Return the difference between x and y."""
        return x - y

    def multiply(self, x, y):
        """Return the product of x and y."""
        return x * y

    def divide(self, x, y):
        """Return the division of x by y. Return an error message for division by zero."""
        try:
            result = x / y
        except ZeroDivisionError:
            return "Error: Division by zero"
        return result

    def display_menu(self):
        """Display a menu of operations."""
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

    def perform_operation(self, choice, x, y):
        """Perform the chosen operation based on user input."""
        if choice == '1':
            return self.add(x, y)
        elif choice == '2':
            return self.subtract(x, y)
        elif choice == '3':
            return self.multiply(x, y)
        elif choice == '4':
            return self.divide(x, y)
        else:
            return "Invalid choice"

def main():
    calc = Calculator()

    calc.display_menu()
    choice = input("Enter choice (1/2/3/4): ")

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return

    result = calc.perform_operation(choice, x, y)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
