# 🐍 Python 1 — heapq, Difficulty: Easy
# Topic: Heap / heapq
# Question : Find the 3 smallest numbers in a list using heapq.
# Example : Input:  [7, 2, 9, 1, 5, 3], Output: [1, 2, 3]
import heapq
nums = [7, 2, 9, 1, 5, 3]
print(heapq.nsmallest(3, nums))

# 🐍 Python 2 — Custom Sorting, Difficulty: Easy–Medium
# Topic: sorted() + lambda
# Question : Sort a list of tuples according to the second element.
# Example : Input:  [("A", 30), ("B", 10), ("C", 20)], Output: [("B", 10), ("C", 20), ("A", 30)]
students = [("A", 30), ("B", 10), ("C", 20)]
students.sort(key=lambda x: x[1])
print(students)
