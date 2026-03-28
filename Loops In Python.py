# Loops in Python

# # While Loop

count = 0
while count < 5: # condition
    print(count)
    count = count + 1

# # print numbers from 1 to 5 using while loop
count = 1
while count < 6: # condition
    print(count)
    count += 1

# # print number from 5 to 1 in descending order.
count = 5
while count > 0: # condition
    print(count)
    count -= 1
else:
    print("while loop endend")

# # Infinite loop 
while True:
    print("again and again!!")

# # For loop 
language = "Python" # sequence 
for x in language:
    print(x)

# Range funcion - range(start, stop, step)
# range(start)
# range (start, stop)
# range(start, stop, step)

for i in range(5):
    print(i)

for i in range (5, 10):
    print(i)

for i in range (1, 10, 2):
    print(i)

for i in range (5):
    print(i)
else:
    print("for loop ended")

# # Loop controls statements
# 1. pass statement

for i in range(5):
    # mann nhi hai 
    pass

count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= 1

# 2. break statement
for i in range(5):
    if i == 3:
        break 
    print(i)

# 3. continue statement 
for i in range(5):
    if i == 3:
        continue
    print(i)

while True:
    user_input = input("enter 'exit' to stop:")
    if user_input == 'exit':
        print("You guessed it right")
        break 
    print("Sorry you entered: ", user_input)
