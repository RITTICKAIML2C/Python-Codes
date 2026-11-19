# 1. Remove Duplicates While Preserving Order
# Given a list, remove duplicate elements without changing the original order.
def remove_duplicates(nums):
  result = []
  seen = set()
  for num in nums:
    if num not in seen:
      result.append(num)
      seen.add(num)
      return result
print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))

# 2. Find the Longest Word in a Sentence
# Given a sentence, find the longest word. If multiple words have the same maximum length, return the first one.
def longest_word(sentence):
  words = sentence.split()
  if not words:
    return ""
    longest = words[0]
    for word in words:
      if len(word) > len(longest):
        longest = word
        return longest
print(longest_word("Python programming is very interesting"))

