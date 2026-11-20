# 1. Find the Missing Elements in a List
# Given a list containing numbers from 1 to n, find all missing numbers.
def find_missing(nums, n):
  present = set(nums)
  result = []
  for num in range(1, n + 1):
    if num not in present:
      result.append(num)
      return result
      print(find_missing([1, 2, 4, 6, 7], 7))

# 2. Compress a String
# Given a string, compress consecutive repeated characters by writing the character followed by its frequency.
def compress_string(s):
  if not s:
    return ""
    result = []
    count = 1
    for i in range(1, len(s)):
      if s[i] == s[i - 1]:
        count += 1
      else:
        result.append(s[i - 1] + str(count))
        count = 1
        result.append(s[-1] + str(count))    
        return "".join(result)
        print(compress_string("aaabbccccdaa"))



Complexity: O(n) time and O(n) space.
