# 🐍 Python 1 — Min Heap Operations, Difficulty: Easy
# Topic: heapq
# Question : Create a min-heap, add a number, and remove the smallest number.
# Example - Input:  [5, 2, 8, 1], Add: 3, Output: Smallest: 1, Heap: [2, 3, 8, 5, ...]
import heapq
nums = [5, 2, 8, 1]
heapq.heapify(nums)
heapq.heappush(nums, 3)
print("Smallest:", heapq.heappop(nums))
print("Heap:", nums)

# 🐍 Python 2 — Top K Largest, Difficulty: Easy–Medium
# Topic: heapq + Problem Solving
# Question : Find the 3 largest numbers in a list using a heap.
# Example : Input:  [10, 4, 7, 2, 15, 8], Output: [10, 15, 8]
import heapq
nums = [10, 4, 7, 2, 15, 8]
result = heapq.nlargest(3, nums)
print(result)
