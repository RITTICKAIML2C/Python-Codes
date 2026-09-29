# 🐍 Python Q1 — Find Common Values in Three Lists
# Question: Find elements that appear in all three lists.
# Input: a = [1,2,3,4,5], b = [2,3,4,6], c = [2,3,7], Output: [2,3] 
a = [1,2,3,4,5]
b = [2,3,4,6]
c = [2,3,7]
result = list(set(a) & set(b) & set(c))
print(result)

# 🐍 Python Q2 — Character Frequency Without Counter
# Question: Count the frequency of every character using a dictionary.
# Input: "banana", Output: {'b': 1, 'a': 3, 'n': 2}
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
