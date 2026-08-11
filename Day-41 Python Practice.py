# 🐍 Python 1 — defaultdict Grouping, Difficulty: Easy
# Topic: defaultdict
# Question - Group numbers based on whether they are even or odd.
# Example : Input:  [1,2,3,4,5,6], Output: {"even": [2,4,6],"odd": [1,3,5]}
from collections import defaultdict
nums = [1,2,3,4,5,6]
groups = defaultdict(list)
for n in nums:
    groups["even" if n % 2 == 0 else "odd"].append(n)
print(dict(groups))

# 🐍 Python 2 — Flatten Nested List, Difficulty: Easy–Medium
# Topic: List Comprehension
# Question : Flatten a 2D list into a single list.
# Example : Input: [[1,2], [3,4], [5,6]], Output : [1,2,3,4,5,6]
matrix = [[1,2], [3,4], [5,6]]
result = [x for row in matrix for x in row]
print(result)
