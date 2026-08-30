# 🐍 Python 1 — Group Anagrams, Difficulty: Easy–Medium
# Topic: Dictionary + Strings
# Question : Group words that are anagrams.
# Input: ["eat","tea","tan","ate","nat","bat"], Output:[["eat","tea","ate"],["tan","nat"],["bat"]]
words = ["eat","tea","tan","ate","nat","bat"]
groups = {}
for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)
print(list(groups.values()))

# 🐍 Python 2 — Two Sum, Difficulty: Medium
# Topic: Dictionary
# Question : Find two indices whose values add up to target.
# Input: nums = [2,7,11,15], target = 9, Output:[0,1]
nums = [2,7,11,15]
target = 9
seen = {}
for i, num in enumerate(nums):
    need = target - num
    if need in seen:
        print([seen[need], i])
        break
    seen[num] = i
