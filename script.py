import random

if __name__ == "__main__":
    random_number = random.randint(0, 10)
    print("Random number:", random_number)

print('I added this. Although it does nothing')

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

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
