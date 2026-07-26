# 🐍 Python Question 1, Difficulty: Easy
# Topic: 2D Lists / Matrix
# Question : Given two matrices, add them and print the resulting matrix.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: Matrix Transpose
# Question : Given a matrix, find its transpose.
matrix = [[1, 2, 3],
          [4, 5, 6]]
transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print(transpose)
