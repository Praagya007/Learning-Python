"""
This script demonstrates basic set concepts and operations in Python.
It covers creating, modifying, and performing various operations on sets.
"""

# --- BASIC SET CONCEPTS ---

# Creating a set
empty_set = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's Length
print(f"Length of fruits set: {len(fruits)}")

# Checking an Item
print(f"Is 'mango' in fruits? {'mango' in fruits}")

# Adding Items to a Set
fruits.add('lime')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)

# Removing Items from a Set
fruits.remove('lime')
fruits.discard('nonexistent fruit') # No error
removed_item = fruits.pop()

# Clearing Items in a Set
fruits.clear()

# Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting List to Set
fruits_list = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits_set = set(fruits_list)


# --- SET OPERATIONS ---

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

# Joining Sets (Union)
union_result = fruits.union(vegetables)
union_result_op = fruits | vegetables

# Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection_result = whole_numbers.intersection(even_numbers)
intersection_result_op = whole_numbers & even_numbers

# Checking Subset and Super Set
print(f"Are even numbers a subset of whole numbers? {even_numbers.issubset(whole_numbers)}")
print(f"Are whole numbers a superset of even numbers? {whole_numbers.issuperset(even_numbers)}")

# Checking the Difference Between Two Sets
difference_result = whole_numbers.difference(even_numbers)
difference_result_op = whole_numbers - even_numbers

# Finding Symmetric Difference Between Two Sets
sym_diff_result = whole_numbers.symmetric_difference({1, 3, 5, 7, 9})
sym_diff_result_op = whole_numbers ^ {1, 3, 5, 7, 9}

# Checking if Sets are Disjoint
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(f"Are even and odd numbers disjoint? {even_numbers.isdisjoint(odd_numbers)}")


# --- EXERCISES ---

# Exercise data
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# --- Level 1 Exercises ---

# 1. Find the length of the set it_companies
print(f"1. Length of it_companies: {len(it_companies)}")

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Nvidia', 'AMD', 'Intel'})

# 4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')

# 5. What is the difference between remove and discard
print("5. Difference between remove() and discard():")
print(" - remove() raises an error if the item doesn't exist")
print(" - discard() doesn't raise an error if the item doesn't exist")

# --- Level 2 Exercises ---

# 1. Join A and B
print(f"1. A union B: {A | B}")

# 2. Find A intersection B
print(f"2. A intersection B: {A & B}")

# 3. Is A subset of B
print(f"3. Is A a subset of B? {A.issubset(B)}")

# 4. Are A and B disjoint sets
print(f"4. Are A and B disjoint? {A.isdisjoint(B)}")

# 5. Join A with B and B with A
A_union_B = A.union(B)
A_copy = A.copy()
A_copy.update(B)

# 6. What is the symmetric difference between A and B
print(f"6. Symmetric difference between A and B: {A ^ B}")

# 7. Delete the sets completely
del A, B

# --- Level 3 Exercises ---

# 1. Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print(f"1. Age list length: {len(age)}")
print(f"   Age set length: {len(age_set)}")

# 2. Explain the difference between string, list, tuple and set
print("2. Differences between data types:")
print(" - String: Immutable sequence of characters enclosed in quotes")
print(" - List: Mutable, ordered sequence that allows duplicates")
print(" - Tuple: Immutable, ordered sequence that allows duplicates")
print(" - Set: Mutable, unordered collection that doesn't allow duplicates")

# 3. Count unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(f"3. Number of unique words: {len(unique_words)}")