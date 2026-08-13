# 🐍 Python 1 — Counter + Sorting, Difficulty: Easy
# Topic: Counter
# Question : Given a string, return its characters sorted by frequency from highest to lowest.
# Example : Input: "tree", Output: "eetr"
from collections import Counter
s = "tree"
freq = Counter(s)
result = "".join(
    ch * count
    for ch, count in freq.most_common()
)
print(result)

# 🐍 Python 2 — Recursive Nested List Sum, Difficulty: Easy–Medium
# Topic: Recursion
# Question : Find the sum of all numbers inside a nested list.
# Example : Input: [1, [2, 3], [4, [5]]], Output: 15
def nested_sum(data):
    total = 0
    for x in data:
        if isinstance(x, list):
            total += nested_sum(x)
        else:
            total += x
    return total
print(nested_sum([1, 2, 3], [4, [5]]]))
