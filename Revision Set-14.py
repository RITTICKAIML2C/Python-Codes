# 1. Print all elements of a list
list = [10, 20, 30, 40, 50]
for lst in list:
    print(lst)

# 2. Find sum of all elements 
list = [5, 8, 12, 7, 3]
sum = 0
for lst in list:
    sum += lst
print(sum)

# 3. Largest element in a list
list = [12, 45, 7, 89, 34]
largest = list[0]
for lst in list:
    if lst > largest:
        largest = lst
print(largest)

# 4. Count evem amnd odd number in a list
list = [10, 23, 44, 55, 60]
even = 0 
odd = 0
for lst in list:
    if lst % 2 == 0:
        even += 1
    else: 
        odd += 1
print(even)
print(odd)

# 5. Reverse a list without using reverse()
list = [1,2,3,4,5]
print(list[::-1])
      or 
reverse_list = []
for i in range(len(list) - 1, -1, -1):
    reverse_list.append(list[i])
print(reverse_list)

# 6. Count how many times an element appears 
list = [1,2,3,2,4,2,5]
lst = list.count(2)
print(f"2 appears {lst} times")

# 7. Remove Duplicates from a list
list = [1,2,2,3,4,4,5]
new_list = []
for lst in list:
    if lst not in new_list:
        new_list.append(lst)
print(new_list)

# 8. List of square using list comprehension
numbers = [1,2,3,4,5]
squares = [num ** 2 for num in numbers]
print(squares)

# 9. Find second largest number
list = [10, 20, 30, 90, 70]
list.sort()
second_largest = list[-2]
print(second_largest)

# 10. Filter even numbers using list comprehension 
numbers = [1,2,3,4,5,6,7,8]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
