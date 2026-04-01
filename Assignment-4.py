# 1. print the while loop output in same line.
i = 1
while i < 4:
    print(f"Hello Madhav {i}", end = " ")
    i += 1

# 2. Star pattern using loops 
# 2.a simple traingle  
# * 
# **
# ***
# ****
# *****
n = 5 # number of rows
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

for i in range(1, n+1):
  print("* " * i)

# 2.b inverted triangle
# *****
# ****
# ***
# **
# *
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

for i in range(n, 0, -1):
  print("* " * i)


# 2.c pyramid pattern
#     *
#    ***
#   *****
#  *******
# *********
n = 5
for i in range(1, n+1):
    print(" " * (n-i), end = " ")
    print("*" * (2 * i - 1))

# 3. write a program to print factorial of a given number
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result 
print(factorial(5))

# 4. Count the number of vowels in a string 
my_string = "Python by Rishabh Mishra"
vowels = "aeiou"
count = 0
for char in my_string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels are", count)

#5. Longest word in a string using for loop
sentence = "Python by Rishabh Mishra"
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

# 6. Do while loop
while True:
    num = int(input("Enter a number greater than 10: "))
    if num > 10:
        print(f"Valid number entered: {num}")
        break
    else:
        print("Number is not greater than 10, try again!")

# 7. Fibonacci Series
def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)
        a, b = b, a+b
        count += 1
fibonacci(5)
