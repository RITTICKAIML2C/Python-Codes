# 🐍 Python 1 — sorted() with key, Difficulty: Easy
# Topic: Sorting + Lambda
# Question ; Sort a list of tuples by the second value.
# Input: [("A", 90), ("B", 70), ("C", 85)]
# Output: [("B", 70), ("C", 85), ("A", 90)]
students = [("A", 90), ("B", 70), ("C", 85)]
result = sorted(students, key=lambda x: x[1])
print(result)

# 🐍 Python 2 — Remove Duplicates While Preserving Order, Difficulty: Medium
# Topic: Sets + Lists
# Question : Remove duplicate values while keeping their original order.
# Input: [4, 2, 4, 1, 2, 3], Output: [4, 2, 1, 3]
nums = [4, 2, 4, 1, 2, 3]
seen = set()
result = []
for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)
print(result)
