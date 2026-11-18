# 1. Rotate a List to the Right
# Given a list and an integer k, rotate the list to the right by k positions.
def rotate_list(nums, k):
  if not nums:
    return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k]
    if k else numsprint(rotate_list([1, 2, 3, 4, 5], 2))

# 2. Find the Most Frequent Element
# Given a list of integers, find the element that appears most frequently.
def most_frequent(nums):
  freq = {}
  for num in nums:
    freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)
    print(most_frequent([1, 3, 2, 3, 4, 3, 2]))
