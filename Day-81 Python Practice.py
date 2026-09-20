# 🐍 Python Q1 — Count Character Types
# Question: Count vowels, consonants, digits, and spaces in a string.
# Input:  "Hello 123". Output: Vowels=2, Consonants=3, Digits=3, Spaces=1
s = "Hello 123"
vowels = consonants = digits = spaces = 0
for ch in s.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
print(vowels, consonants, digits, spaces)

# 🐍 Python Q2 — Group Numbers by Frequency
# Question: Group numbers according to how many times they occur.
# Input:  [1, 2, 2, 3, 3, 3, 4], Output: {1: [1], 2: [2], 3: [3], 1: [4]}
from collections import defaultdict, Counter
nums = [1, 2, 2, 3, 3, 3, 4]
freq = Counter(nums)
result = defaultdict(list)
for num, count in freq.items():
    result[count].append(num)

print(dict(result))
