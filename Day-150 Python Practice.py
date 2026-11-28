# Python 1 — Find All Pairs With a Given Sum
def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)
print(find_pairs([1, 5, 7, -1, 5, 3, 3], 6))

# Python 2 — Rotate a Matrix 90 Degrees Clockwise
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = (
                matrix[j][i],
                matrix[i][j]
            )
    for row in matrix:
        row.reverse()
    return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
