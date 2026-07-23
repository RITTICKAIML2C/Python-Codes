# 🐍 Python Question 1, Difficulty: Easy
# Topic: Functions + Strings
# Question : Write a function is_palindrome(s) that returns True if the given string is a palindrome, otherwise False.
# Example : Input - madam, Output - True
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
text = input("Enter a string: ")
print(is_palindrome(text))

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: Dictionaries
# Question : Given a sentence, print the frequency of each word.
# Example : Input - python is easy python is fun, Output - python : 2, is : 2, easy : 1, fun : 1
sentence = input("Enter sentence: ").split()
freq = {}
for word in sentence:
    freq[word] = freq.get(word, 0) + 1
for key, value in freq.items():
    print(key, ":", value)
