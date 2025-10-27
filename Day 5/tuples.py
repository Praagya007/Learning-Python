# ===== Exercise 1 =====

# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and brothers
sisters = ('Anna', 'Maria')
brothers = ('John', 'Peter')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("\nSiblings:", siblings)

# 4. How many siblings do you have?
print("Number of siblings:", len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother
family_members = siblings + ('Father', 'Mother')
print("Family members:", family_members)


# ===== Exercise 2 =====

# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print("\nUnpacked siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

# 2. Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'tomato', 'onion')
animal_products = ('milk', 'cheese', 'egg')

# 3. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("\nFood stuff tuple:", food_stuff_tp)

# 4. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 5. Slice out the middle item(s) from the food_stuff_lt list
length = len(food_stuff_lt)
middle_index = length // 2
if length % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1: middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("\nMiddle item(s):", middle_items)

# 6. Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 7. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# (Trying to print food_stuff_tp now would cause an error)

# 8. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("\nIs 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)
