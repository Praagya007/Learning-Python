# Import necessary modules
import datetime

# ==================== CREATING DICTIONARIES ====================

# Empty dictionary
empty_dict = {}

# Dictionary with initial values
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# ==================== ACCESSING DICTIONARY ITEMS ====================

# Access using square brackets (will raise KeyError if key doesn't exist)
first_name = person['first_name']
country = person['country']
skills = person['skills']
first_skill = person['skills'][0]
street = person['address']['street']

# Access using get() method (safer - returns None if key doesn't exist)
first_name_safe = person.get('first_name')
city = person.get('city')  # Returns None

# ==================== DICTIONARY LENGTH ====================

person_length = len(person)

# ==================== ADDING AND MODIFYING ITEMS ====================

# Adding new items
person['job_title'] = 'Instructor'
person['skills'].append('HTML')

# Modifying existing items
person['first_name'] = 'Eyob'
person['age'] = 252

# ==================== CHECKING KEYS ====================

# Check if a key exists
has_age = 'age' in person
has_city = 'city' in person

# ==================== REMOVING ITEMS ====================

# Create a copy for demonstration
person_copy = person.copy()

# Using pop() - removes the item with the specified key and returns its value
removed_job = person_copy.pop('job_title')

# Using popitem() - removes the last item
removed_item = person_copy.popitem()

# Using del - removes an item with the specified key
del person_copy['is_married']

# ==================== DICTIONARY METHODS ====================

# Getting keys as a list
keys = list(person.keys())

# Getting values as a list
values = list(person.values())

# Getting items as a list of tuples
items = list(person.items())

# ==================== CLEARING AND DELETING ====================

# Clearing a dictionary
temp_dict = {'a': 1, 'b': 2}
temp_dict.clear()

# Deleting a dictionary completely
original = {'a': 1, 'b': 2}
del original

# ==================== COPYING A DICTIONARY ====================

# Create a dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Copy using copy() method - creates a true copy
copied_dict = original_dict.copy()
copied_dict['d'] = 4

# Note: Using assignment operator just creates another reference
reference_dict = original_dict
reference_dict['e'] = 5  # This also modifies original_dict

# ==================== WORKING WITH LISTS IN DICTIONARIES ====================

my_info = {
    'name': "James",
    'favorite_color': "black", 
    'hobbies': ["Coding", "Researching", "Deep thinking"]
}

# Using list methods on dictionary values
my_info['hobbies'].extend(["Reading", "Running"])
my_info['hobbies'].insert(1, "Meditation")
my_info['hobbies'].reverse()
my_info['hobbies'].clear()
my_info['hobbies'].extend(["Yoga", "Swimming", "Traveling"])

# ==================== NESTED DICTIONARIES ====================

contacts = {
    'friends': [
        {'name': 'Alice', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob', 'phone': '234-567-8901', 'email': 'bob@example.com'}
    ],
    'family': [
        {'name': 'Charlie', 'phone': '345-678-9012', 'email': 'charlie@example.com'},
        {'name': 'Dana', 'phone': '456-789-0123', 'email': 'dana@example.com'}
    ]
}

# Adding a new friend
contacts['friends'].append({'name': 'Eve', 'phone': '567-890-1234', 'email': 'eve@example.com'})

# Changing Bob's phone number
for friend in contacts['friends']:
    if friend['name'] == 'Bob':
        friend['phone'] = '999-888-7777'

# Getting family names using list comprehension
family_names = [member['name'] for member in contacts['family']]

# ==================== EXERCISES ====================

# Exercise 1: Create an empty dictionary called dog
dog = {}

# Exercise 2: Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 5
}

# Exercise 3: Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        'street': '123 Main St',
        'zipcode': '10001'
    }
}

# Exercise 4: Get the length of the student dictionary
student_length = len(student)

# Exercise 5: Get the value of skills and check the data type
skills = student['skills']
skills_type = type(skills)

# Exercise 6: Modify the skills values by adding one or two skills
student['skills'].extend(['React', 'Node.js'])

# Exercise 7: Get the dictionary keys as a list
student_keys = list(student.keys())

# Exercise 8: Get the dictionary values as a list
student_values = list(student.values())

# Exercise 9: Change the dictionary to a list of tuples using items() method
student_items = list(student.items())

# Exercise 10: Delete one of the items in the dictionary
del student['marital_status']

# Exercise 11: Delete one of the dictionaries
del dog

# ==================== COMPUTER EXAMPLE ====================

# Create the initial dictionary
computer = {
    "brand": "Acer",
    "model": "Nitro V16",
    "ram": 16,
    "storage": 512,
    "has_ssd": True,
    "price": 1200,
    "Generation": 14
}

# Add the current year to the dictionary
current_year = datetime.datetime.now().year
computer["year_made"] = current_year

# Increase the price by 10%
computer["price"] *= 1.10

# Check the RAM and print a message
if computer["ram"] >= 8 and computer["Generation"] > 12:
    print("This computer has excellent performance with at least 8GB of RAM! Ideal for coding")
else:
    print("This computer may not be ideal for heavy tasks.")

# Convert to a list of tuples and print
computer_tuples = list(computer.items())

# ==================== FINAL CHALLENGE ====================

# Create a book dictionary
book = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'year_published': 1925,
    'genres': ['Novel', 'Fiction', 'Classic'],
    'rating': 4.5
}

# Add a new key called available with a boolean value
book['available'] = True

# Update the rating by 0.1
book['rating'] += 0.1

# Check if the book was published after 2000 and print a message
if book['year_published'] > 2000:
    print("This is a modern book.")
else:
    print("This is a classic book.")

# Print just the genres as a list
book_genres = book['genres']