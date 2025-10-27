# ============================
# Exercises: Level 1
# ============================

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']

# 3. Find the length of your list
print("Length of items list:", len(items))

# 4. Get the first item, the middle item and the last item of the list
first_item = items[0]
middle_item = items[len(items)//2]
last_item = items[-1]
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# 5. Declare a list called mixed_data_types
mixed_data_types = ['John Doe', 28, 1.75, 'Single', '123 Main Street']
print("Mixed data types:", mixed_data_types)

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print("IT Companies:", it_companies)

# 8. Print the number of companies
print("Number of IT companies:", len(it_companies))

# 9. Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies)//2])
print("Last company:", it_companies[-1])

# 10. Modify one of the companies
it_companies[2] = 'Microsoft Corp'
print("After modification:", it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Intel')
print("After adding Intel:", it_companies)

# 12. Insert an IT company in the middle
it_companies.insert(len(it_companies)//2, 'Samsung')
print("After inserting Samsung in the middle:", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded)
it_companies[0] = it_companies[0].upper()
print("After changing first company to uppercase:", it_companies)

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print("Joined companies:", joined_companies)

# 15. Check if a certain company exists
print("Is Google in the list?", 'Google' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print("Sorted companies:", it_companies)

# 17. Reverse the list in descending order
it_companies.reverse()
print("Reversed companies:", it_companies)

# 18. Slice out the first 3 companies
print("First 3 companies:", it_companies[:3])

# 19. Slice out the last 3 companies
print("Last 3 companies:", it_companies[-3:])

# 20. Slice out the middle IT company or companies
middle_index = len(it_companies)//2 #8/2=4
if len(it_companies) % 2 == 0: 
    print("Middle companies:", it_companies[middle_index-1:middle_index+1]) #Slice from 3 to 5, meaning 4.
else:
    print("Middle company:", it_companies[middle_index])

# 21. Remove the first IT company
it_companies.pop(0)
print("After removing first company:", it_companies)

# 22. Remove the middle IT company or companies
middle_index = len(it_companies)//2
it_companies.pop(middle_index)
print("After removing middle company:", it_companies)

# 23. Remove the last IT company
it_companies.pop(-1)
print("After removing last company:", it_companies)

# 24. Remove all IT companies
it_companies.clear()
print("After clearing list:", it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Joined full stack:", full_stack)

# 27. Copy the joined list and insert Python and SQL after Redux
full_stack_copy = full_stack.copy()
redux_index = full_stack_copy.index('Redux')
full_stack_copy[redux_index+1:redux_index+1] = ['Python', 'SQL']
print("Full stack after inserting Python and SQL:", full_stack_copy)


# ============================
# Exercises: Level 2
# ============================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort and find min, max
ages.sort()
print("Sorted ages:", ages)
min_age, max_age = min(ages), max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# 2. Add min and max again
ages.extend([min_age, max_age])
print("Ages after adding min and max again:", ages)

# 3. Find the median age
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Median age:", median)

# 4. Find the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# 5. Find the range of the ages
age_range = max_age - min_age
print("Age range:", age_range)

# 6. Compare (min - average) and (max - average), abs: absolute
print("absolute(min - average):", abs(min_age - average_age)) 
print("absolute(max - average):", abs(max_age - average_age))

# 7. Find the middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries)//2
if len(countries) % 2 == 0:
    print("Middle countries:", countries[middle_index-1:middle_index+1])
else:
    print("Middle country:", countries[middle_index])

# 8. Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print("First half:", first_half)
print("Second half:", second_half)

# 9. Unpack the first three countries and the rest as scandic countries
china, russia, usa, *scandic_countries = countries
print("China:", china)
print("Russia:", russia)
print("USA:", usa)
print("Scandic countries:", scandic_countries)