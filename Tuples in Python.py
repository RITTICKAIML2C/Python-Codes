# Tuples in Python 

my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

# Create tuples
# 1. Using paranthesis
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))

my_tuple1 = (1, "Madhav", True, 3.14)
print(my_tuple1)

# 2. Without paranthesis
tuple1 = 1,2,3
print(tuple1)
print(type(tuple1))

# 3. Tuple Constructor 
tuple2 = tuple((1,5,9))
print(type(tuple2))
print(tuple2)

list1 = [1,2,3]
new_tuple = tuple(list1)
print(new_tuple)

# 4. Create a single element
a = ("a",)
print(type(a))

# Tuple Indexing 
fruits = ("apple", "mango", "cherry")
print(fruits[0])

print(fruits[-1])

# Tuple Slicing
new_tuple = (10, 20, 30, 40, 50)
print(new_tuple[0:3:1])
print(new_tuple[0:3:2])

# Tuple Operations 
# 1. concatenate - join tuples 
tuple1 = (1,2,3)
tuple2 = ('a', 'b')
tuple3 = tuple1 + tuple2 
print(tuple3)

# 2. Repititon
tuple2 = ('a', 'b') * 2
print(tuple2)

# 3. Checking for an item.
tuple22 = (1,2,3)
print(10 in tuple22)

# Tuple Iteration 
# 1. for loops 
fruits = ('apple', 'mango', 'cherry')
for i in fruits:
    print(i)

# 2. while loops 
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Tuple Methods 
color = ('blue', 'green', 'orange', 'blue')

# count 
print(color.count('blue'))

# index 
print(color.index('green'))

# Tuple functions 
numbers = (2, 3, 1, 4)

# len 
print(len(numbers))
# sum 
print(sum(numbers))
# min() and max()
print(min(numbers))
print(max(numbers))

# sort
a = sorted(numbers)  # tuple is now list
numbers_sorted = tuple(a)
print(numbers_sorted)

# Tuples Packing and Unpacking 
a = "Madhav"
b = 21
c = "Engineer"

tuple_pack = a,b,c
print(tuple_pack)

name, age, profession = tuple_pack
print("Name is", name)
print(age)
print(profession)

# Tuple Modification 
tuple_numbers = (10, 20, 30)
tuple_numbers[0] = 100  # Error

# # how to mutate/modify tuple 
list_numbers = list(tuple_numbers)
print(list_numbers)

list_numbers[0] = 100
print(list_numbers)

tuple_numbers = tuple(list_numbers)
print(tuple_numbers)
