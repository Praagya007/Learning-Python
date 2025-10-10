# helloworld.py
import sys #provides access to some variables and functions that interact with the Python runtime environmen
import math


# 1. Check Python version
print("Python version:", sys.version)

# 2. Perform basic operations with 3 and 4
print("Addition:", 3 + 4)
print("Subtraction:", 3 - 4)
print("Multiplication:", 3 * 4)
print("Modulus:", 3 % 4)
print("Division:", 3 / 4)
print("Exponential:", 3 ** 4)
print("Floor Division:", 3 // 4)

# 3. Print strings
print("John")           # Your first name
print("Doe")            # Your last name
print("USA")            # Your country
print("I am enjoying 30 days of python")

#Python data types
# Integer
x = 5
print("Integer:", x, type(x))

# Float
y = 3.14
print("Float:", y, type(y))

# Complex
z = 4 - 4j
print("Complex:", z, type(z))

# String
name = "John"
print("String:", name, type(name))

# Boolean
is_python_fun = True
print("Boolean:", is_python_fun, type(is_python_fun))

# List
languages = ["Python", "Java", "C++"]
print("List:", languages, type(languages))

# Tuple
coordinates = (10, 20, 30)
print("Tuple:", coordinates, type(coordinates))

# Set
unique_numbers = {1, 2, 3, 4, 5}
print("Set:", unique_numbers, type(unique_numbers))

# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary:", person, type(person))


# Coordinates
x1, y1 = 2, 3
x2, y2 = 10, 8

# Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance:", distance)
