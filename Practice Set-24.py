# 1. Function even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(10))

# 2. Function : sum of list 
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_list([1,2,3,4]))

# 3. Function : Find largest number in list
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
print(find_largest([1,2,3,4]))

# 4. Function : count vowels in string 
def count_vowels(s):
    count = 0
    vowel = "aeiouAEIOU"
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("programming"))

# 5. Function : reverse a number
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print(reverse_number(1234)) 

# 6. Function : check prime number
def prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime_number(7))

# 7. Function: factorial 
def fact(n):
    count = 1
    for i in range(1, n+1):
        count = count * i 
    return count
print(fact(5))

# 8. Function : Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(5))

# 9. Function : frequency of characters (Dict + Func)
def freq(n):
    freq = {}
    for ch in n:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
print(freq("banana"))

# 10. Function : merge two dictionaries 
def merge_dicts(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result 
print(merge_dicts({'a' : 1, 'b' : 2}, {'b' : 3, 'c' : 4}))

# 11. Function with *args return sum of all numbers passed 
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3, 4))

# 12. Function with **kwargs 
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
print_details(name = "Rittick", age = 18, city = "London")

# 13. Function : student result system 
students = {
    "Rittick" : 85, 
    "Aman" : 92, 
    "Raj" : 67
}
def get_topper(data):
    return max(data, key=data.get), max(data.values())
def get_average(data):
    return sum(data.values()) / len(data)
def get_high_scorers(data):
    return [name for name, marks in data.items() if marks >= 80]
print(get_topper(students))
print(get_average(students))
print(get_high_scorers(students))
