# 1. Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# 2. Mulitplication Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 3. Count digits in a number
num = int(input("Enter a number: "))
count = 0 
while num != 0:
    num = num // 10
    count += 1
print("Total count =", count)

# 4. Reverse a number
n = int(input("Enter a number: "))
rev = 0 
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed Number:", rev)

# 5. Count Vowels 
text = "I Love Python Programming"
char = "aeiouAEIOU"
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print("Total vowels =", count)

# 6. Reverse a string without slicing 
n = input("Enter a string: ")
rev = ""
for i in range(len(n)-1, -1, -1):
    rev += n[i]
print(rev)

# 7. Check Palindrome string 
n = input("Enter a string: ")
s = n[::-1]
if n == s:
    print(f"{n} is Palindrome")
else:
    print(f"{n} is not Palindrome")

# 8. Longest Word in a Sentence
s = input("Enter a sentence: ")
words = s.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

# 9. Sum of List elements 
numbers = [10, 20, 30, 40]
sum = 0
for n in numbers:
    sum += n
print("Sum is:", sum)

# 10. Largest in the list
numbers = [12, 45, 7, 89, 34]
longest = numbers[0]
for n in numbers:
    if n > longest:
        longest = n
print('Longest=', longest)

# 11. Remove Duplicates from list
list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for lst in list:
    if lst not in new_list:
        new_list.append(lst)
print(new_list)

# 12. Find second Largest numbers
numbers = [10, 50, 30, 90, 70]
numbers.sort()
print("Second Largest =", numbers[-2])

# 13. Find maximum elements 
t = (10, 25, 5, 40, 15)
print("Maximum =", max(t))

# 14. Tuple unpacking 
t = (100, 200, 300)
a, b, c = t
print("A =", a)
print("B =", b)
print("C =", c)

# 15. Remove duplicates from set 
numbers = [1, 2, 2, 3, 4, 4, 5]
s = set(numbers)
print(s)

# 16. Common elements between two lists 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
common_elements = set(list1) & set(list2)
print(common_elements)

# 17. Unique Characters in String 
words = "Programming"
s = set(words)
print(s)

# 18. Count even and odd numbers in a list
numbers = [10, 23, 44, 55, 60, 71]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even number :", even)
print("Odd numbers :", odd)
