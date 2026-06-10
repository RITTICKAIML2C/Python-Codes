# 1. create and Print a set
my_set = (10, 20, 30, 40, 50)
print(my_set)

# 2. Remove Duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]
new_set = set(numbers)
print(new_set)

# 3. Length of a set 
s = {5, 10, 15, 20, 25}
print(len(s))

# 4. Add an element to a set
s = {1, 2, 3, 4}
s.add(5)
print(s)

# 5. Remove an elements from a set
s = {10, 20, 30, 40}
s.discard(20)
print(s)

# 6. Check if an element exists
s = {5, 10, 15, 20}
if 15 in s:
    print("Element Found")
else:
    print("Element not Found")

# 7. Union of Two Sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union_set = a | b
print(union_set)

# 8. Intersection of Two Sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersection_set = a & b
print(intersection_set)

# 9. Difference of two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
difference_set = a - b
print(difference_set)

# 10. Symmteric Difference 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
symmetric_difference = a ^ b
print(symmetric_difference)

# 11. Iterate through a set
s = {'apple', 'banana', 'mango'}
for i in s:
    print(i)

# 12. Convert string to set 
word = "programming"
new_set = set(word)
print(new_set)

# 13. Find common elements between two lists 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
new_set = set(list1) & set(list2)
print(new_set)

# 14. Check subset 
a = {1, 2}
b = {1, 2, 3, 4}
if a <= b:
    print("A is a subset of B")
else: 
    print("A is not subset of B")

# 15. Set Comprehension 
squares = {x**2 for x in range(1,6)}
print(squares)

# 16. Count unique elements in a list.
nums = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_count = len(set(nums))
print(unique_count)

# 17. Find unique vowels in a string.
word = "programming is amazing"
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {ch for ch in word if ch in vowels}
print(found_vowels)
