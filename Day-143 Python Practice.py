# 1. Find the Pair With the Given Difference
def has_pair_difference(nums, k):
    seen = set()
    for num in nums:
        if num - k in seen or num + k in seen:
            return True
        seen.add(num)
    return False
print(has_pair_difference([1, 5, 3, 4, 2], 2))

# 2. Find the Longest Consecutive Sequence in a List
def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0
    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1
            while current + 1 in numbers:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
