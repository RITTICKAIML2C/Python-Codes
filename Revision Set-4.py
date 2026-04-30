 1. Sum of even number in list.
def even_sum(n):
    d = 0
    for s in n:
        if s % 2 == 0:
            d += s
    return d
print(even_sum([1,2,3,4,5,6]))

# 2. Function to count digits using function 
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count 
print(count_digits(1234))

# 3. Function to check palindrome number 
def palindrome(n):
    num = str(n)
    rev = num[::-1]
    if num == rev:
        return True
    else:
        return False
print(palindrome(121))

# 4. Functions: Second Largest Number
def second_largest(nums):
    largest = nums[0]
    second = nums[0]
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
print(second_largest([10, 20, 30]))

# 5. Function : Remove duplicates from a list
def remove_duplicates(n):
    new_list = []
    for lst in n:
        if lst not in new_list:
            new_list.append(lst)
    return new_list
print(remove_duplicates([1,2,2,3,3,4]))

# 6. Function : count frequency of words
def count_freq(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(count_freq("I Love Python I Love Coding"))

# 7. Function: find common elements between two lists.
def common_elem(d1, d2):
    new_list = []
    for num in d1:
        if num in d2:
            new_list.append(num)
    return new_list
print(common_elem([1,2,3,4], [3,4,5,6]))

# 8. Functions: check armstrong numbers
def armstrong(num):
    n = str(num)
    power = len(n)
    total = 0
    for digit in n:
        total += int(digit) ** power
    if total == num:
        return True
    else:
        return False
print(armstrong(153))

# 9. Function: Create dicitonary from Two lists
def dictionary(k, v):
    d = {}
    for i in range(len(k)):
        d[k[i]] = v[i]
    return d
print(dictionary(['a', 'b', 'c'], [1, 2, 3]))

# 10. Function : Group words by length 
def group_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result 
print(group_length(['hi', 'hello', 'hey', 'python']))
    
# 11. Function : find all prime numbers in range
def find_primes(start, end):
    primes = [] 
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(find_primes(1, 20))

# 12. Function: calculator using *args
def calculator(operation, *args):
    if operation == "add":
        total = 0
        for num in args:
            total += num
        return total 
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
print(calculator("add", 1, 2, 3))

# 13. Function : Nested Function
def outer(name):
    def inner():
        return "Hello " + name
    return inner()
print(outer("Rittick"))

# 14. Mini Project : Student Data System 
students = {
    "Rittick" : [85, 90, 88], 
    "Aman" : [92, 80, 85],
    "Raj" : [60, 70, 65]
}
def get_average(data):
    marks = students[data]
    total = 0
    for m in marks:
        total += m 
    return total / len(marks)

def get_topper():
    top_name = ""
    highest_avg = 0
    for name in students:
        avg = get_average(name)
        if avg > highest_avg:
            highest_avg = avg
            top_name = name
    return top_name

def get_failed():
    failed = []
    for name in students:
        avg = get_average(name)
        if avg < 70:
            failed.append(name)
    return failed

print(get_average("Rittick"))
print(get_topper())
print(get_failed())
