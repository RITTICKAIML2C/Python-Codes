# 1. Default Argument Practice
# Create: def greet(name, message="Welcome"):
# If only name is given → use default message.
# If message is provided → override it.
def greet(name, message="Welcome"):
    return f"{message}, {name}!"
print(greet("Rittick","Good Morning"))

# 2. Positional vs Keyword Arguments
# Create: def student_info(name, age, course):
# Call this function: Once using positional arguments, Once using keyword arguments, Once by mixing both (correct order)
# Function definition
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student_info("Aman", 22, "Python")
student_info(name="Aman", age=22, course="Python")
student_info("Aman", age=22, course="Python")

# 3. Function with *args
# Create: def find_sum(*numbers):
# Return the sum of all numbers passed.
def find_sum(*numbers):
    return sum(numbers)
result = find_sum(1,2,3,4,5,6)
print(result)

# 4. Function with **kwargs
# Create: def print_details(**info):
# Print each key and value.
def print_details(**info):
    for key, value in info.items():
        print(f"{key}:{value}")
print_details(name = "Aman", age = 21, city = "Delhi")

# 5. Combine Default + *args
# Create: def multiply_numbers(multiplier=1, *numbers):
# Multiply each number by multiplier and return total sum.
def multiply_numbers(multiplier=1, *numbers):
    total = 0
    for num in numbers:
        total += multiplier * num
    return total

# 6. Return vs Modify (Important Thinking Question)
# Create: def add_to_list(my_list, element):
# Append element to list and return updated list.
def add_to_list(my_list, element):
    my_list.append(element)
    return my_list

# 7. Mini Challenge (Very Important)
# Create: def calculator(operation, *numbers):
# If operation is: "add" → sum all numbers, "multiply" → multiply all numbers, anything else → return "Invalid"
def calculator(operation, *numbers):
    if operation == "add":
        total = 0
        for num in numbers:
            total += num
        return total
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        return "Invalid"

