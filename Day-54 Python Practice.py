# 🐍 Python 1 — Sort Dictionary by Value, Difficulty: Easy
# Topic: Dictionaries + sorted()
# Question : Sort a dictionary by its values from smallest to largest.
# Input: {"a": 5, "b": 2, "c": 8}, Output: {"b": 2, "a": 5, "c": 8}
data = {"a": 5, "b": 2, "c": 8}
result = dict(sorted(data.items(), key=lambda x: x[1]))
print(result)

# 🐍 Python 2 — Longest Word in a Sentence, Difficulty: Easy–Medium
# Topic: Strings + Lists
# Question : Find the longest word in a sentence.
# Input: "I love learning Python programming", Output: "programming"
sentence = "I love learning Python programming"
words = sentence.split()
longest = max(words, key=len)
print(longest)
