# 🐍 Python Q1 — Find Second Smallest Unique Number
# Question: Find the second smallest unique number in a list.
# Input:  [5, 2, 8, 2, 1, 5, 3], Output: 2
nums = [5, 2, 8, 2, 1, 5, 3]
unique = sorted(set(nums))
print(unique[1])

# 🐍 Python Q2 — Group Anagrams
# Question: Group words that are anagrams of each other.
# Input:  ["eat", "tea", "tan", "ate", "nat", "bat"], Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
from collections import defaultdict
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for word in words:
    groups[''.join(sorted(word))].append(word)
print(list(groups.values()))
