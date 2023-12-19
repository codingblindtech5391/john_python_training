# Conditionals Example

# If statement
number = 10
if number > 0:
    print(f"{number} is a positive number.")

# If-else statement
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not too hot.")

# If-elif-else statement
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Nested if statements
is_weekend = True
temperature = 28
if is_weekend:
    if temperature > 25:
        print("It's a hot weekend.")
    else:
        print("It's a pleasant weekend.")
else:
    print("It's a weekday.")

# Ternary conditional expression
age = 15
category = "Teenager" if age >= 13 and age <= 19 else "Not a Teenager"
print(category)
