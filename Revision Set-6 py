# 1. Frequency of digits in a number
n = 122334
freq = {}
while n > 0:
    d = n % 10
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1
    n = n // 10
print(freq)

# 2. Count Vowels Using Dictionary 
words = "programming"
vowels = "aeiouAEIOU"
freq = {}
for ch in words:
    if ch in vowels:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print(freq)

# 3. Merge two dictionaries 
d1 = {'a' : 1, 'b' : 2}
d2 = {'b' : 3, 'c' : 4}
result = {}
for key in d1:
        result[key] += d1[key]
for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]
print(result)

# 4. Find key with minimum value
marks = {'maths' : 85, 'science' : 92, 'english' : 78}
minimum = min(marks, key=marks.get)
print(minimum)

# 5. Character position tracker
text = "banana"
result = {}
for i in range(len(text)):
    ch = text[i]
    if ch in result:
        result[ch].append(i)
    else:
        result[ch] = [i]
print(result)

# 6. Invert Dictionary 
d = {'a' : 1, 'b' : 2, 'c' : 1}
result = {}
for key in d:
    value = d[key]
    if value in result:
        result[value].append(key)
    else:
        result[value] = [key]
print(result)

# 7. Count word starting with each letter
text = "apple banana avocado berry"
result = {}
words = text.split()
for ch in words:
    first = ch[0]
    if first in result:
        result[first] += 1
    else:
        result[first] = 1
print(result)

# 8. Sort dictionary by values
d = {'a' : 3, 'b' : 1, 'c' : 2}
sort = dict(sorted(d.items()))
print(sort)

# 9. Find common keys in two dictionaries 
d1 = {'a' : 1, 'b' : 2, 'c' : 3}
d2 = {'b' : 5, 'c' : 7, 'd' : 9}
result = {}
for key in d1:
    if key in d2:
        result[key] = d1[key]
print(result)

# 10. Build Student Result System (Mini Project)
students = {
    "Rittick" : 85,
    "Aman" : 92, 
    "Raj" : 67
}
topper = max(students, key=students.get)
avg = sum(students.values()) / len(students)
print("Topper:", topper)
print("Average:", avg)
for name in students:
    if students[name] > 80:
        print("High scorer:", name)
