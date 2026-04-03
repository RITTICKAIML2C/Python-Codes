# 1. Create a function that print number from 1 to n
def function(n):
    for i in range(1, n+1):
        print(i)
function(7)

# 2. Function to Find Sum of First N Numbers
def number(n):
    sum = 0 
    for i in range(1, n+1):
        sum += i
    return sum
print(number(4))

# 3. Function to Check Even or Odd
def evenodd(n):
    for i in range(n):
        if n % 2 == 0:
            return "Even"
        return "Odd"
print(evenodd(4))

# 4. Function to find factorial 
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

# 5. Function to count digits in a number
def count_digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count 
print(count_digit(45891))

# 6. Function to Find Largest of Three Numbers
def largest(a,b,c):
    while max > a:
        if a > b and a > c:
            return "A is largest"
        elif b > a and b > c:
            return "B is largest"
        return "C is largest"
print(largest(4,9,2))


# 7. Function to print multiplication table
def multiply(n):
    for i in range(1, 11):
        print(n,"x",i,"=", n*i)
multiply(5)

# 8. Function to Check Prime Number
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return "Not prime"
        return "Prime"
print(is_prime(7))

# 9. Function to print Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(6)

# 10. Function to Reverse a Number
def reverse_number(n):
    count = 0
    while n != 0:
        digit = n % 10
        count = count * 10 + digit
        n = n // 10
    return count
print(reverse_number(1234))
