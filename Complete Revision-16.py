# 1. Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

# 2. Multiplication Table 
num = int(input("Enter a number: "))
for i in range(1, 11):
print(f"{num} x {i} = {num * i}")
    
# 3. Count Digits in a Number
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Total digits =", count)

# 4. Reverse a number
n = int(input("Enter a number: "))
rev = 0 
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed Number:", rev)

# 5. Count vowels in a string
code = "I Love Python Programming"
char = "aeiouAEIOU"
count = 0
for char in code:
    if char in "aeiouAEIOU":
        count += 1
print("Total vowels:", count)

# 6. Palindrome String Checkher
string = input("Enter a string: ")
string_reverse = string[::-1]
if string == string_reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Print all elements of a list.
list = [10,20,30,40,50]
count = 0
for lst in list:
    count += lst
    print(lst)

# 8. Find largest element in a list
list = [12,45,7,89,34]
largest = list[0]
for lst in list:
    if lst > largest:
        largest = lst
print("Largest element:", largest)

# 9. Sum of even numbers in a list
list = [1,2,3,4,5,6,7,8]
even = 0
for lst in list:
    if lst % 2 == 0:
        even = even + lst
print("Sum of even numbers is:", even)

# 10. Remove Duplicates from list
list = [1,2,2,3,4,4,5]
new_list = []
for lst in list:
    if lst not in new_list:
        new_list.append(lst)
print(new_list)

# 11. Second largest number
list = [10, 50, 30, 90, 70]
list.sort()
second_largest = list[-2]
print("Second Largest:", second_largest)
