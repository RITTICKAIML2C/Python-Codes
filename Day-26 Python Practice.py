# 🐍 Python Question 1, Difficulty: Easy
# Topic: Nested Lists
# Question : Given a nested list, find the sum of all elements.
# Example : Input:[[1,2,3], [4,5], [6]], Output: 21
nums = [[1, 2, 3], [4, 5], [6]]
total = 0
for row in nums:
    for num in row:
        total += num
print(total)

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: Nested Lists + Searching
# Question : Find the largest element in each row of a matrix.
# Example : Input:[[1,5,3],[8,2,4],[6,9,1]], Output: [5,8,9
matrix = [[1, 5, 3],
          [8, 2, 4],
          [6, 9, 1]]
result = []
for row in matrix:
    result.append(max(row))
print(result)
