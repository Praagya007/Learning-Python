# Day 2: 30 Days of Python programming
import math #Importing math library for mathematical calculations.

# Declaring variables
first_name = "John"
last_name = "Doe"
full_name = "John Doe"
country = "USA"
city = "New York"
age = 30
year = 2025
is_married = False
is_true = True
is_light_on = False

# Declaring multiple variables on one line
a, b, c = 1, 2, 3

# Check the data types of the variables
print("Type of first_name:", type(first_name))
print("Type of last_name:", type(last_name))
print("Type of full_name:", type(full_name))
print("Type of country:", type(country))
print("Type of city:", type(city))
print("Type of age:", type(age))
print("Type of year:", type(year))
print("Type of is_married:", type(is_married))
print("Type of is_true:", type(is_true))
print("Type of is_light_on:", type(is_light_on))

# Length of first name
first_name_length = len(first_name)
print("Length of first name:", first_name_length)

# Compare lengths
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are of the same length.")

# Declare num_one and num_two
num_one = 5
num_two = 4

# Perform arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Print results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)


# Radius of circle
radius = 30

# Area of circle (πr²)
area_of_circle = math.pi * (radius ** 2)
print("Area of circle:", area_of_circle)

# Circumference of circle (2πr)
circum_of_circle = 2 * math.pi * radius
print("Circumference of circle:", circum_of_circle)

# Radius of the circle
radius = 30

# Area of circle (πr²)
area_of_circle = math.pi * (radius ** 2)
print(f"Area of circle: {area_of_circle:.2f}")

# Circumference of circle (2πr)
circum_of_circle = 2 * math.pi * radius
print(f"Circumference of circle: {circum_of_circle:.2f}")


#6. Get radius using user input.
radius=float(input("Enter a number: "));
areaOfCircle=math.pi*radius**2;
print(f"{areaOfCircle:.2f}")

#7. Get first name, last name, country, and age as user input:

# User input
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

print(f"Name: {user_first_name} {user_last_name}")
print(f"Country: {user_country}")
print(f"Age: {user_age}")

#8. To check for reserved keywords
help('keywords');