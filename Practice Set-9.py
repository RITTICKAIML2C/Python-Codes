# 1. Sum of Digits of a Number
# Example: Input: 4567, Output: 22
# Concept: Digit extraction + accumulator
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    n = n // 10
    sum += digit
print("Sum of digits are:", sum)

# 2. Product of Digits
# Example: Input: 234, Output: 24
n = int(input("Enter a number: "))
product = 1
while n > 0:
    digit = n % 10
    n = n // 10
    product *= digit
print("Product of digits:", product)

# 3. Count digits divisible by 3
# 1236 → 2 digits (3 and 6)
count = 0
for i in range(1, 100):
    if i % 3 == 0:
        count += 1
print("Number of digits:", count)

# 4. Prime Number Check
# Example: 7 → Prime
# Concept: Loop from 2 to n-1
n = int(input("Enter a number: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime number")
else:
    print("Not prime")

# 5. Fibonacci Series (First N Terms)
# Example: 0 1 1 2 3 5 8
# Concept: Variable shifting
n = int(input("How many numbers: "))
a = 0
b = 1
for i in range(n):
    print(a)
    next_num = a + b
    a = b
    b = next_num
