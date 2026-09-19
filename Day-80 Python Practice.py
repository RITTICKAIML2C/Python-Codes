# 🐍 Python Q1 — Find Common Elements
# Question: Find elements present in both lists, without duplicates.
# Input:  [1, 2, 3, 4], [3, 4, 5, 6], Output: [3, 4]
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(list(set(a) & set(b)))

# 🐍 Python Q2 — Group Words by Length
# Question: Group words according to their length.
# Input:  ["cat", "apple", "dog", "hi", "book"], Output: {3: ["cat", "dog"], 5: ["apple"], 2: ["hi"], 4: ["book"]}
words = ["cat", "apple", "dog", "hi", "book"]
result = {}
for word in words:
    result.setdefault(len(word), []).append(word)
print(result)
