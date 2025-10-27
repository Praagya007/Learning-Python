# 1. Concatenate strings
part1 = 'Thirty'
part2 = 'Days'
part3 = 'Of'
part4 = 'Python'
sentence1 = part1 + ' ' + part2 + ' ' + part3 + ' ' + part4
print(sentence1)  # Thirty Days Of Python

# 2. Concatenate the string 'Coding', 'For', 'All'
sentence2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(sentence2)  # Coding For All

# 3. Declare variable
company = "Coding For All"

# 4. Print company
print(company)

# 5. Print length
print(len(company))

# 6. Uppercase
print(company.upper())

# 7. Lowercase
print(company.lower())

# 8. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut the first word
print(company[7:])  # Removes 'Coding '

# 10. Check if contains 'Coding'
print('Coding' in company)
print(company.find('Coding'))
print(company.index('Coding'))

# 11. Replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# 12. Replace in a new string
new_str = 'Python for Everyone'
print(new_str.replace('Everyone', 'All'))

# 13. Split using space
print(company.split()) #Splits string into multiples in an array.

# 14. Split at comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(','))

# 15. Character at index 0
print(company[0])

# 16. Last index
print(len(company) - 1)

# 17. Character at index 10
print(company[10]) #The output is a space since its the 10th char.

# 18. Create acronym for 'Python For Everyone'
phrase1 = 'Python For Everyone'
acronym1 = ''.join(word[0] for word in phrase1.split())
print(acronym1)  # PFE

# 19. Create acronym for 'Coding For All'
phrase2 = 'Coding For All'
acronym2 = ''.join(word[0] for word in phrase2.split())
print(acronym2)  # CFA

# 20. Index of first occurrence of 'C' in 'Coding For All'
print(phrase2.index('C'))  # 0

# 21. Index of first occurrence of 'F' in 'Coding For All'
print(phrase2.index('F'))  # 7

# 22. rfind() - last occurrence of 'l' in 'Coding For All People'
text3 = 'Coding For All People'
print(text3.rfind('l'))  # 19

# 23. Find the first occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  # 31

# 24. Find the last occurrence of 'because'
print(sentence.rindex('because'))  # 47

# 25. Slice out 'because because because'
words=sentence.split()
extracted=" ".join(words[6:9])
print(extracted)

# 26. Does it start with 'Coding'?
print(company.startswith('Coding'))

# 27. Does it end with 'coding'?
print(company.endswith('coding'))

# 28. Remove left and right spaces
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip()) #Similar to .trim in JS.

# 29. Which one is a valid identifier?
print('30DaysOfPython'.isidentifier())       # False
print('thirty_days_of_python'.isidentifier()) # True

# 30. Join list with hash and space
frameworks = ['Django', 'Flask', 'Fast API', 'PyTorch', 'Pydantic']
print(' # '.join(frameworks)) 

# 31. New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32. Tab escape sequence
print("Name\t\tAge\tCountry\tCity\nPraagya\t18\tNepal\tKathmandu")

# 33. String formatting for area
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

# 34. String formatting for arithmetic
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

