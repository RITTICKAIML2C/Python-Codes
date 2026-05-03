# 1. Create and print dicitonary 
dict = {
    'name' : 'Raj',
    'age' : 20,
    'city' : 'Kolkata'
}
print(dict)

# 2. Access Values
student = {'name' : 'Rittick', 'age' : 18, 'marks' : 85}
print(student['name'])
print(student['marks'])

# 3. Add a New key 
student = {
    'name' : 'Rittick',
    'age' : 18,
}
student['grade'] = 'A'
print(student)

# 4. Update value 
student = {
    'name' : 'Rittick',
    'age' : 18,
    'marks' : 85
}
student['marks'] = 90
print(student)

# 5. Remove a key
student = {
    'name' : 'Rittick',
    'age' : 18,
}
new_student = student.pop('age')
print(student)

# 6. Check if key exists 
student = {
    'name' : 'Rittick',
    'age' : 18,
}
if 'name' in student:
    print("Key exists")
else:
    print("Key not found")

# 7. Iterate through dictionary. Print all keys, values, key-value
student = {
    'name' : 'Rittick',
    'age' : 18,
}

# a. all keys 
for key in student:
    print(key)

# b. all values
for values in student:
    print(student[values])

# c. all key-value pairs
for key, value in student.items():
    print(key, value)

# 8. Count frequency of Characters 
word = "programming"
freq = {}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
        
# 9. Count frequency of words
text = "I Love Python and I love Coding"
words = text.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

# 10. Find Maximum value key 
marks = {'maths' : 85, "science" : 92, "english" : 88}
highest = max(marks, key=marks.get)
print(highest)

# 11. Sum of all values 
d = {'a' : 10, 'b' : 20, 'c' : 30}
sum = 0
for dic in d:
    sum += d[dic]
print("Sum =", sum)

# 12. Merge two dictionaries
d1 = {
    'a' : 1, 
    'b' : 2
}
d2 = {
    'c' : 3, 
    'd' : 4
}

# Method : 1 
d3 = d1 | d2
print(d3)

# Methods : 2
d1.update(d2)
print(d1)
    
# 13. Remove duplicates from list using dictionary 
nums = [1, 2, 2, 3, 4, 4, 5]
seen = {}
result = []
for num in nums:
    if num not in seen:
        seen[num] = True
        result.append(num)
print(result)

# 14. Dictionary comprehension of square 
square = {x : x*x for x in range(1, 6)}
print(square)

# 15. Nested Dictionary Access 
student = {
    'name' : 'Rittick', 
    'marks' : {'math' : 90, "science" : 85}
}
print(student['marks']['math'])
print(student['marks']['science'])

# 16. Find first non repeating character 
word = 'aabbcdeff'
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
for ch in word:
    if freq[ch] == 1:
        print(ch)
        break

# 17. Group Numbers by Even/Odd
nums = [1, 2, 3, 4, 5, 6]
dict = {'even' : [], 'odd' : []}
for num in nums:
    if num % 2 == 0:
        dict['even'].append(num)
    else:
        dict['odd'].append(num)
print(dict)
