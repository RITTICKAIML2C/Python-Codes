# 1. Print all elements in tuple
numbers = (10, 20, 30, 40, 50)
for num in numbers:
    print(num)

# 2. Find length of tuple
t = (5, 8, 12, 7, 3)
print(len(t))

# 3. Find Maximum element 
t = (12, 45, 7, 89, 34)
print("Maximun element:", max(t))

# 4. Count Occurence of an element
t = (1, 2, 3, 2, 4, 2, 5)
print("2 appears", t.count(2), "times")

# 5. Convert list to tuple
numbers = [10, 20, 30, 40]
new_tuple = tuple(numbers)
print(new_tuple)

# 6. Tuple Unpacking 
t = (10, 20, 30)
a, b, c = t
print(a)
print(b)
print(c)

# 7. Swap Two numbers using tuple 
a = 5 
b = 10
a, b = b, a
print("a =", a)
print("b =", b)

# 8. Access element in nested tuple 
t = (1, 2, (3, 4, 5), 6)
print(t[2][1])

# 9. Find sum of elements 
tuple = (10, 20, 30, 40)
total = 0 
for i in tuple:
    total += i
print("Sum =", total)

# 10. Check if elements exists in tuple
t = (5, 10, 15, 20)
if 15 in t:
    print("Element found")
else:
    print("Element not found")

# 11. Covert tuple into list then modify to tuple
t = (1, 2, 3, 4)
l = list(t)
l.append(5)
t = tuple(l)
print(t)
