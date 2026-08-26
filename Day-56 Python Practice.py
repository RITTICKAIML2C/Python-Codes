# 🐍 Python 1 — zip(), Difficulty: Easy
# Topic: zip() + Lists
# Question ; Combine two lists into a dictionary.
# Input: keys = ["a", "b", "c"], values = [10, 20, 30]
# Output: {"a": 10, "b": 20, "c": 30}
keys = ["a", "b", "c"]
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

# 🐍 Python 2 — Most Common Character, Difficulty: Medium
# Topic: Dictionary + Strings
# Question : Find the character that appears most often.
# Input: "programming", Output: "r"
s = "programming"
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(max(count, key=count.get))
