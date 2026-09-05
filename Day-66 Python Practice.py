# 🐍 Python 1 — Count Vowels, Difficulty: Easy
s = "programming"
vowels = "aeiou"
count = sum(ch in vowels for ch in s.lower())
print(count)

# 🐍 Python 2 — Sort a Dictionary by Value, Difficulty: Medium
data = {"a": 3, "b": 1, "c": 2}
result = dict(sorted(data.items(), key=lambda x: x[1]))
print(result)
