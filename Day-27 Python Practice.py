# 🐍 Python 1 — Counter, Difficulty: Easy
# Topic: collections.Counter
# Question : Given a string, count how many times each character appears.
# Example : Input:  banana, Output: {'b': 1, 'a': 3, 'n': 2}
from collections import Counter
s = input("Enter string: ")
count = Counter(s)
print(count)

# 🐍 Python 2 — defaultdict, Difficulty: Easy–Medium
# Topic: Dictionary / defaultdict
# Question : Group words according to their first letter.
# Example : Input: ["apple", "ant", "ball", "bat"]
from collections import defaultdict
words = ["apple", "ant", "ball", "bat"]
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))
