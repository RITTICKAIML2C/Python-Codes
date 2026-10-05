# 🐍 Python Q1 — Invert a Dictionary
# Convert keys into values and values into keys.
# Input: {"a": 1, "b": 2, "c": 3} Output: {1: "a", 2: "b", 3: "c"}
data = {"a": 1, "b": 2, "c": 3}
result = {value: key for key, value in data.items()}
print(result)

# 🐍 Python Q2 — Find the Longest Word
# Find the longest word in a sentence. If there is a tie, return the first one.
# Input: "I love solving programming problems", Output: "programming"
sentence = "I love solving programming problems"
words = sentence.split()
longest = max(words, key=len)
print(longest)
