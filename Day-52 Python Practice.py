# 🐍 Python 1 — Dictionary Word Count, Difficulty: Easy
# Topic: Dictionaries
# Question : Count how many times each word appears.
# Input:["cat", "dog", "cat", "bird", "dog", "cat"], Output:{"cat": 3, "dog": 2, "bird": 1}
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# 🐍 Python 2 — Merge Two Dictionaries, Difficulty: Easy–Medium
# Topic: Dictionaries
# Question : Merge two dictionaries. If a key exists in both, add their values.
# Input: a = {"a": 10, "b": 20}, b = {"b": 30, "c": 40}, Output: {"a": 10, "b": 50, "c": 40}
a = {"a": 10, "b": 20}
b = {"b": 30, "c": 40}
result = a.copy()
for key, value in b.items():
    result[key] = result.get(key, 0) + value
print(result)
