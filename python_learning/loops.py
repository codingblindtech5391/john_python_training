# Loops Example

# For loop
print("For loop:")
for i in range(5):
    print(i)

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Looping through a list
print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string
print("\nLooping through a string:")
word = "Python"
for letter in word:
    print(letter)

# Break statement
print("\nBreak statement:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
print("\nContinue statement:")
for i in range(5):
    if i == 2:
        continue
    print(i)
