# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Tuples
# Problem Statement - Write a program to find the largest and smallest element in a tuple without using the max() or min() functions.
# Example : Input - 10 45 3 89 21, Output - Largest = 89, Smallest = 3
numbers = tuple(map(int, input("Enter a number: ").split()))
largest = numbers[0]
smallest = numbers[0]
for num in numbers: 
  if num > largest:
    largest = num
  if num < smallest:
    smallest = num
print("Largest =", largest)
print("Smallest =", smallest)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: File Handling
# Problem Statement - Write a program to create a file named student.txt, write the text "Hello, Python!" into it, close the file, then open the file again and print its contents.
# Example: Output - Hello, Python!
file = open("student.txt", "w")
file.write("Hello, Python!")
file.close()
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()
