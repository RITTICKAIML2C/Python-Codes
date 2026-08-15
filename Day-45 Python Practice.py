# 🐍 Python 1 — zip(), Difficulty: Easy
# Topic: zip()
# Question : Combine two lists into a dictionary.
# Input: names = ["A", "B", "C"], marks = [80, 90, 85]
# Output: {"A": 80, "B": 90, "C": 85}
names = ["A", "B", "C"]
marks = [80, 90, 85]
result = dict(zip(names, marks))
print(result)

# 🐍 Python 2 — Find Missing Number, Difficulty: Easy–Medium
# Topic: Sets
# Question : Find the missing number from 1 to n.
# Input:  [1, 2, 4, 5], Output: 3
nums = [1, 2, 4, 5]
n = len(nums) + 1
result = set(range(1, n + 1)) - set(nums)
print(result.pop())
