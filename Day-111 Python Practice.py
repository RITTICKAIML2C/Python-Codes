# 🐍 Q1 — Python: Find Common Dictionary Keys
# Task: Find keys present in both dictionaries.
# Input: a = {"x": 1, "y": 2, "z": 3}b = {"y": 5, "z": 6, "w": 7}
# Output: {'y', 'z'}
a = {"x": 1, "y": 2, "z": 3}
b = {"y": 5, "z": 6, "w": 7}
print(a.keys() & b.keys())


# 🐍 Q2 — Python: Find the Longest Word
# Task: Find the longest word in a sentence.
# Input: "Python makes coding enjoyable"
# Output: "enjoyable"
text = "Python makes coding enjoyable"
print(max(text.split(), key=len))
