# Python 1 — Move All Zeros to the End
def move_zeros(nums):
    position = 0
    for num in nums:
        if num != 0:
            nums[position] = num
            position += 1
    while position < len(nums):
        nums[position] = 0
        position += 1
    return nums
print(move_zeros([0, 1, 0, 3, 12]))

# Python 2 — Find the Most Frequent Element
def most_frequent(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)
print(most_frequent([4, 2, 4, 3, 2, 2, 4]))
