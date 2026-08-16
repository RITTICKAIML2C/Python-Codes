# 🐍 Python 1 — heapq, Difficulty: Easy
# Topic: Min Heap
# Question : Find the 3 smallest numbers using a heap.
# Input:  [7, 2, 9, 1, 5], Output: [1, 2, 5]
import heapq
nums = [7, 2, 9, 1, 5]
heapq.heapify(nums)
result = [heapq.heappop(nums) for _ in range(3)]
print(result)

# 🐍 Python 2 — Top K Frequent Elements, Difficulty: Medium
# Topic: Counter + Heap
# Question : Find the k most frequent elements.
# Input: nums = [1,1,1,2,2,3], k = 2, Output : [1,2]
from collections import Counter
nums = [1,1,1,2,2,3]
k = 2
freq = Counter(nums)
print([x for x, _ in freq.most_common(k)])
