# Functions Example

# Simple function without parameters
def greet():
    print("Hello, welcome!")

# Function with parameters
def square(number):
    return number * number

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

# Function with a docstring
def print_info(name, age):
    """
    Prints information about a person.

    Parameters:
    - name (str): The person's name.
    - age (int): The person's age.
    """
    print(f"Name: {name}")
    print(f"Age: {age}")

# Calling functions
greet()

result = square(5)
print(f"Square of 5 is: {result}")

power_result = power(2)
print(f"2 to the power of 2 is: {power_result}")

print_info("Alice", 30)
