# 1. Print the sum of numbers between 1 and 100 that are divisible by 5.
sum = 0
for i in range(1, 101):
    if i % 5 == 0:
        sum += i
print("Sum of numbers divisible by 5: ", sum)

# 2. Count how many numbers between 1 and n are divisibe by 3 and 7 both
n = 100
count = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 7 == 0:
        count += 1
print(count)

# 3. Pattern problme 
# 1
# 12
# 123
# 1234
# 12345
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()

# 4. Reverse Pattern
# 12345
# 1234
# 123
# 12
# 1
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end = "")
    print()

# 5. Number Triangle 
# 1 
# 22 
# 333
# 4444
# 55555
n = 5 
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end = "")
    print()

# 6. Print all prime number between 1 and 50
for n in range(2, 51):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

# 7. Strong Number 
num = 145
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    temp //= 10
if sum == num:
    print("Strong Number")
else:
    print("Not Strong Number")
