# Dictionary in Python.

# Syntax:
# my_dict = {'key1':'value1', 'key2':'value2', ...}

# Methods to create dictionary

# method-1 create dictionary using curly braces {}
cohort = {'course':'Python', 
          'Intstructor':'Rittic Mishra', 
          'Level':'Beginner'}
print(cohort)
print(type(cohort))


# Method-2 using dict() constructor
person = dict(name = 'Raj', age = 20, grade = 'A')
print(person)
print(type(person))

# Method-3 using list of tuples
person2 = dict([('name', 'Raj'), ('age', 20), ('city', 'Kolkata')])
print(person2)
print(type(person2))

# Access Dictionary Values
student = {
    1: 'Class-X',
    'name': 'Raj',
    'grade': 'A',
    'city': 'Kolkata'
}
print(student)
print(type(student))

print(student['name'])
print(student['grade'])


# Dictionary Methods 
student = {
    1: 'Class-X',
    'name': 'Raj',
    'grade': 'A',
    'city': 'Kolkata'
}

# keys
print(student.keys())

# values
print(student.values())

# items 
print(student.items())

# get
print(student.get('name'))
print(student.get('email', 'Nahi hai'))


# Add / Modify items in dictionary
student = {
    'name': 'Raj',
    'grade': 'A',
    'city': 'Kolkata'
}

# add item - assign operator (=)
student['email'] = 'raj@example.com'
print(student)

# modify / replace item - assign operator (=)
student['grade'] = 'A+'
print(student)

# remove items
# 1. del to remove item
del student['grade']
print(student)

# 2. pop method 
var1 = student.pop('email')
print(var1)
print(student)


# Dictionary Iteration 
student = {
    'name': 'Raj',
    'grade': 'A',
    'city': 'Kolkata', 
}

# loop through keys 
for keys in student:
    print(keys)

# loop through values
for values in student:
    print(values)

# using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair 
for keys, value in student.items():
    print(keys, value)


# Nested Dictionary 
main_student = {

    'student1' : {'name' : 'Raj', 'age' : 20},
    'student2' : {'name' : 'Rittick', 'age' : 25, 'grade' : 'A'}

}

print(main_student)

# access value
print(main_student['student1'])

print(main_student['student1']['name'])
print(main_student['student2']['name'])


# Dictionary Comprehension 

# syntax
new_dict = {key_expression : value_expression for item in iterable if condition}

# Squares of numbers using dict comprehension
my_dict = {x:x*x for x in range(1, 6)}

# print(my_dict)
