# 1. Print numbers divisible by 4 between 1 and n
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 4 == 0:
        print(i)

# 2. Count numbers divisible by boith 3 and 5
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 3. Function to return sum of digits of a number
def sum_numbers(n):
    count = 0
    while n > 0:
        digit = n % 10
        count += digit
        n = n // 10
    return count
print(sum_numbers(234))

# 4. Function to check if a number is palindrome
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return original == reverse
n = int(input("Enter number: ")) 
if is_palindrome(n):
    print("True")
else:
    print("False")

# 5. Largest digit in a number

# 6. Function to print Fibonacci series up to n terms
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a,b = b, a+b
fibonacci(6)

# 7. Function to print Fibonacci series up to n terms
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not prime"
        return "Prime"
print(prime(7))

# 9. Create a calculator function 
def calculator(operation, a, b):
    if operation == "add":
        return a + b    
    elif operation == "sub":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Can't divide by zero"
        return a / b
    else:
        return "Invalid Operation"
print(calculator("add",5,3))
print(calculator("sub",5,3))
print(calculator("multiply",5,3))
print(calculator("divide",5,3))

# 10. Count how many prime number exist between 1 and n
def prime(n):
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            return "Not prime"
        else:
            count = count + 1
            return count 
print(prime(100))
