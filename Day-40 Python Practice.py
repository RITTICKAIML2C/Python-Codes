# 🐍 Python 1 — defaultdict, Difficulty: Easy
# Topic: collections.defaultdict
# Question : Count the frequency of each character using defaultdict.
# Example : Input:  "hello", Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
from collections import defaultdict
s = "hello"
freq = defaultdict(int)
for ch in s:
    freq[ch] += 1
print(dict(freq))

# 🐍 Python 2 — Group Words by Length, Difficulty: Easy–Medium
# Topic: defaultdict + Lists
# Question : Group words according to their length.
# Example : Input: ["cat", "dog", "apple", "bat", "banana"], Output:{3: ["cat", "dog", "bat"],5: ["apple"],6: ["banana"]}
from collections import defaultdict
words = ["cat", "dog", "apple", "bat", "banana"]
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
print(dict(groups))
