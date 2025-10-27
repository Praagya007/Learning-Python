# 💻 Day 3 Exercises

# 1. Declare your age as an integer variable
age = 25

# 2. Declare your height as a float variable
height = 1.75

# 3. Declare a variable that stores a complex number
complex_num = 3 + 4j

# 4. Calculate area of a triangle
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base * height_triangle
print(f"The area of the triangle is {area_triangle}")

# 5. Calculate perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# 6. Rectangle area and perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_rectangle}")

# 7. Circle area and circumference
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of the circle is {area_circle}")
print(f"The circumference of the circle is {circumference}")

# 8. y = 2x - 2
# slope (m) = 2, y-intercept = -2, x-intercept = ?
m = 2
y_intercept = -2
x_intercept = y_intercept / -m
print(f"Slope: {m}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")

# 9. Slope and distance between (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope between (2,2) and (6,10): {slope_2}")
print(f"Euclidean distance: {distance}")

# 10. Compare slopes
print(f"Comparison of slopes: slope_1 = {m}, slope_2 = {slope_2}")

# 11. Find x when y = 0 for y = x^2 + 6x + 9
# y = (x + 3)^2 => y = 0 when x = -3
x_values = [-3, -2, 0, 1, 2]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"When x = {x}, y = {y}")

print("y is 0 when x = -3")

# 12. Length comparison
len_python = len("python")
len_dragon = len("dragon")
print(len_python, len_dragon)
print("Is length of python != dragon?", len_python != len_dragon)

# 13. Check if 'on' is found in both words
print("'on' in python and dragon:", "on" in "python" and "on" in "dragon")

# 14. Check for 'jargon' in a sentence
sentence = "I hope this course is not full of jargon."
print("jargon in sentence:", "jargon" in sentence)

# 15. There is no 'on' in both dragon and python
print("There is no 'on' in both:", not ("on" in "dragon" and "on" in "python"))

# 16. Convert length of 'python' to float then to string
length = len("python")
length_float = float(length)
length_str = str(length_float)
print(length_float, type(length_str))

# 17. Check even number
num = int(input("Enter a number: "))
print(f"{num} is even? {num % 2 == 0}")

# 18. Floor division of 7 by 3 == int(2.7)
print(7 // 3 == int(2.7))

# 19. Check type equality
print(type('10') == type(10))

# 20. Check if int('9.8') == 10
try:
    print(int('9.8') == 10)
except ValueError:
    print("Cannot convert '9.8' directly to int")

# 21. Calculate weekly earning
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earning = hours * rate
print(f"Your weekly earning is {earning}")

# 22. Calculate total seconds lived
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

#23. Display table.
for n in range(1,6):
    print(n,1,n,n**2,n**3)
