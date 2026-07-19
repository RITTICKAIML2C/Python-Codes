# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Regular Expressions (re module)
# Problem Statement : Write a program to check whether the word "Python" exists in a given sentence using the re module.
# Example : Input - I am learning Python programming, Output - Word Found
import re
sentence = input("Enter a sentence: ")
result = re.search("Python", sentence)
if result:
    print("Word Found")
else:
    print("Word Not Found")

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Regular Expressions (re.findall())
# Problem Statement : Given a sentence, find all the numbers present in it using Regular Expressions.
# Example : Input - Rahul scored 95 marks in 2025, Output - ['95', '2025']
import re
sentence = input("Enter a sentence: ")
numbers = re.findall(r"\d+", sentence)
print(numbers)
