# operators in python 

# 1. Arithmetic Operators 
a = 5
b = 3
print(a+b)  # Addition operator 
print(a-b)  # Substraction operator
print(a*b)  # Multiplication operator
print(a%b)  # Modulus operator

# 2. Comparison Operators - output is boolean value(T/F) 
a = 5
b = 3
print(a>b) # greater than operator
print(a<b) # lesser than operator
print(a == b) # equals operator 
print(a != b) # not equals operator

# 3. Assignment Operator
a = 5 # assignment operator

# 4. Logical Operator 
# Rule (For AND Operator)
# 1. True + True = False
# 2. True + False = False
# 3. False + False = False 
a = 10
b = 20
print(a>10 and a<10) # and operator
print(a==10 and a==20)
# Rule for OR operator
#True + False = True 
print(a==10 or b<10) # or operator 
print(not(a==10 and b==20))

# 5. Identity Operator - is, is not
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y) # is operator 
print(x is z) # is operator
print(x is not z) # is not operator

# 6. Membership Operators - in, not in
my_list = {'apple', 'orange', 'watermelon'}
print('apple' in my_list) # in operator
print('apple2' in my_list) 
print('apple2' not in my_list) # not in operator

# 7. Bitwise Operator - AND &, OR |, XOR ^, NOT ~, etc
a = 5        # 5 in binary - 0101 
b = 3        # 3 in binary - 0011
print(a & b) # 1 in binary - 0001
