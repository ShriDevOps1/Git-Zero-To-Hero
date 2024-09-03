def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Example usage
x = 10
y = 5

print(f"Addition: {x} + {y} = {add(x, y)}")
print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
print(f"Division: {x} / {y} = {divide(x, y)}")
