# Python 1 — Transpose a Matrix
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result
matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose(matrix))

# Python 2 — Group Words That Are Anagrams
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
