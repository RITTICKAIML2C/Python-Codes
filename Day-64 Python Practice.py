# 🐍 Python 1 — Remove Duplicates While Preserving Order, Difficulty: Easy
nums = [1, 2, 2, 3, 1, 4]
result = list(dict.fromkeys(nums))
print(result)

# 🐍 Python 2 — Longest Word, Difficulty: Medium
# Find the longest word in a sentence.
s = "Python is very powerful and versatile"
words = s.split()
longest = max(words, key=len)
print(longest)
