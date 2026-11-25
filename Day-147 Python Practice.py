# Python 1 — Find the Second Largest Unique Number
def second_largest(nums):
    first = float('-inf')
    second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return None if second == float('-inf') else second
print(second_largest([10, 5, 20, 8, 20, 15]))

# Python 2 — Count Substrings With Equal First and Last Characters
def count_substrings(s):
    freq = {}
    result = 0
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        result += freq[char]
    return result


print(count_substrings("abcab"))
