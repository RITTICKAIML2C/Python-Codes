# 🐍 Python 1 — Find Common Keys in Two Dictionaries
a = {"x": 10, "y": 20, "z": 30}
b = {"w": 40, "y": 50, "z": 60}
common = a.keys() & b.keys()
print(common)

# 🐍 Python 2 — Find the Longest Consecutive Sequence
nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
longest = 0
for num in s:
    if num - 1 not in s:
        length = 1
        while num + length in s:
            length += 1
        longest = max(longest, length)
print(longest)
