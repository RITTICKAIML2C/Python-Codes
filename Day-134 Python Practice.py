# Exercise 1 — Find the second-largest distinct element
# Write a Python function that returns the second-largest distinct number in a list.
def second_largest(nums):
  unique_nums = list(set(nums))
  if len(unique_nums) < 2:
    return None
  unique_nums.sort(reverse=True)
  return unique_nums[1]
print(second_largest([10, 5, 20, 8, 20]))

# Exercise 2 — Rotate a list to the right by K positions
def rotate_list(nums, k):
  if not nums:
    return nums
  k = k % len(nums)
  return nums[-k:] + nums[:-k] if k else nums
print(rotate_list([1, 2, 3, 4, 5], 2))

