# 1. Print Numbers 1 to 10
# for loop

for i in range (1, 11):
    print(i)

# 2. Print Even Numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 3. Print Numbers From 10 to 1 (Reverse Order)
for i in range(10, 0, -1):
    print(i)

# 4. Sum of first 10 natural number.
n = int(input("Enter a number: "))
count = 0
for i in range(1, n+1):
    count = count + i
print("Sum is: ", count)

# 5. Multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i )

# 6. Sum of even numbers from 1 to 100
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += i

print("Sum:", count)

# 7. Count digits in a number 
n = abs(n)
if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

# 8. Reverse a Number
# Problem: Input: 12345, Output: 54321
n = int(input("Enter a number: "))
count = 0
while n != 0:
    digit = n % 10
    count = count * 10 + digit
    n = n // 10
print("Reverse number:", count)

# 9. Palindrome Number
# Check if a number reads the same forward and backward.
# 121 → Palindrome, 123 → Not
n = int(input("Enter a number: "))
original = n
reverse = 0
while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 10. Factorial of a Number
# Problem: 5! = 5 × 4 × 3 × 2 × 1
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print("Factorial of number is:", factorial)

# 11. Count Even and Odd Digits in a Number
# Input: 45231, Even digits = 2, Odd digits = 3
n = int(input("Enter a number: "))
even = 0
odd = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print("Even digit:", even)
print("Odd digit:", odd)

# 12. Find the Largest Digit in a Number
# Input : 73952
# Output: Largest digit = 9
n = int(input("Enter a number: "))
largest = 0
while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit
    n = n // 10
print("Largest digit", largest)
