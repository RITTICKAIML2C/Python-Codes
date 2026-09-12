# 🐍 Python 1 — Find the Missing Number
nums = [1, 2, 3, 5, 6]
n = len(nums) + 1
missing = sum(range(1, n + 1)) - sum(nums)
print(missing)

# 🐍 Python 2 — Group Words by Their First Letter
words = ["apple", "banana", "ant", "ball", "cat"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)
