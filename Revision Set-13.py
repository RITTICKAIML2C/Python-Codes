# 1. Find the smallest element in a list
numbers = [25, 10, 45, 5, 30]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)

# 2. Count positive and negative numbers
numbers = [3, -2, 7, -5, 10, -8]
positive = 0
negative = 0
for num in numbers:
    if num > 0:
        positive += 1
    else:
        negative += 1
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)


# 3. Sum of even numbers only 
numbers = [1,2,3,4,5,6,7,8]
even = 0
for num in numbers:
    if num % 2 == 0:
        even += num
print("Sum of even numbers:", even)

# 4. Remove all even numbers from a list. 
numbers = [1,2,3,4,5,6]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num)
print(new_list)

# 5. Find the avergae of list elements
numbers = [10, 20, 30, 40, 50]
avg = 0
length = len(numbers)
for num in numbers:
    if num > 0:
        avg += num
print(f"Average = {avg / length}")
#           or 
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
avg = total / len(numbers)
print(avg)

# 6. Find the largest and smallest in one loop
numbers = [12, 45, 7, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
