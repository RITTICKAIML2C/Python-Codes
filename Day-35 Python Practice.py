# 🐍 Python Question 1, Difficulty: Easy
# Topic: itertools.permutations()
# Question : Print all permutations of a string.
# Example : Input : s = "ABC", Output : ABC ACB BAC BCA CAB CBA
from itertools import permutations
s = "ABC"
for p in permutations(s):
    print("".join(p))

🐍#  Python Question 2, Difficulty: Easy–Medium
# Topic: itertools.combinations()
# Question : Print all combinations of 2 elements from a list.
# Example : Input : nums = [1, 2, 3, 4], Output : (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
from itertools import combinations
nums = [1, 2, 3, 4]
for c in combinations(nums, 2):
    print(c)
