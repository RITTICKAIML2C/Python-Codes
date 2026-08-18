# 🐍 Python 1 — map() + filter(), Difficulty: Easy
# Topic: Functional Python
# Question : From a list, keep only even numbers and square them.
# Input:  [1,2,3,4,5,6], Output: [4,16,36]
nums = [1,2,3,4,5,6]
result = list(map(lambda x: x*x,
                  filter(lambda x: x % 2 == 0, nums)))
print(result)

# 🐍 Python 2 — Group Anagrams, Difficulty: Medium
# Topic: Dictionary + Strings
# Question : Group words that are anagrams
# Input: ["eat","tea","tan","ate","nat","bat"], Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
words = ["eat","tea","tan","ate","nat","bat"]
groups = {}
for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
print(list(groups.values()))
