# 🐍 Python 1 — Reverse Words in a Sentence, Difficulty: Easy
# Topic: Strings
# Question : Reverse the order of words.
# Input:  "I love Python", Output: "Python love I"
s = "I love Python"
result = " ".join(s.split()[::-1])
print(result)

# 🐍 Python 2 — Prefix Sum Range Query, Difficulty: Medium
# Topic: Arrays + Prefix Sum
# Question : Find the sum from index left to right.
# nums = [2, 4, 1, 5, 3], left = 1, right = 3, Output: 10
nums = [2, 4, 1, 5, 3]
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
left = 1
right = 3
result = prefix[right + 1] - prefix[left]
print(result)
