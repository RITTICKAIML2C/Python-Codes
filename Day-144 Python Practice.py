# Python 1 — Rotate a List to the Right
def rotate_list(nums, k):
    if not nums:
        return nums
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
nums = [1, 2, 3, 4, 5]
print(rotate_list(nums, 2))

# Python 2 — Find the First Non-Repeating Character
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None
print(first_unique_char("aabbcde"))
