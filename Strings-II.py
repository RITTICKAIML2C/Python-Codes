# # String in Python
# # strings - single, double, triple quotes

name = "Madhav" # creating a string
print(name)

print(type(name)) # checking datatype

print("It's Easy")
print("Hello World")

print('''"kw-double Quotes"''')

print("\"kw-double Quotes\" " )

# # Formatted strings 
# # 1. Old style formatting - % operator

name = "Madhav"
age = 16
print("My name is %s and I'm %d" %(name, age))
# # %s, %d are placeholders for the string and integers

# # 2. Str.format() method

name = "Madhav"
age = 16
print("My name is {} and I'm {}".format(name, age))


# # you can refernce variable by index or code
print("My name is {0} and I'm {1}".format(name, age))
print("My name is {1} and I'm {0}".format(name, age))

print("My name is {name} and I'm {age}".format(name="Keshav", age=21))

# # 3. f-strings 
name = "Rishabh"
age = 24
print(f"My name is {name} and I'm {age}")

print(f"My age after 5 years will be {age + 5}")

# # Escape characters - backslash with characters 
print(''' "kw-double quotes" ''')

print(" \"kw-double quotes\" ") # double quotes using backslash

print(" \'kw-single quotes\' ") # single quotes using backslash

print("Hello\nWorld")       # new line
print("Hello\tWorld")       # tab - space

# String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)  # concatenate
print(a*2)  # multiple copies
# # [] - slice , [i] - range -- scroll below

if "H" in a:
    print("yes")
else:
    print("no")

print(r"Hello\nWorld")  # Raw string : suppress the escape characters 

# String Indexing 
my_name = "MADHAV"
# index:   012345
print(my_name[0])   # first character of string
print(my_name[1])   # second character of string
print(my_name[2])   # third character of string
print(my_name[3])   # fourth character of string
print(my_name[4])   # fifth character of string
print(my_name[5])   # sixth character of string

name2 = "Hello World"
# index: 012345678910
print(name2[4])
print(name2[5])     # blank space is also a character
print(name2[-1])    # last char from str
print(name2[-3])    # 3rd last char from str

# String Slicing
syntax : string[start : end : stop]
my_name = "MADHAV"
# index: 012345

print(my_name[0:3])     # default step = 1
print(my_name[0:3:1])
print(my_name[0:5:1])
print(my_name[3:5:1])
print(my_name[0:5:2])   # step = 2
print(my_name[0:5:3])   # step = 3
print(my_name[0:5:4])   # step = 4
print(my_name[0:2])     # first 2 characters
print(my_name[0:3])     # first 3 characters
print(my_name[2:5])     # third to fifth character 

print(my_name[-1:])     # last char of str
print(my_name[5:])      # last char of str
print(my_name[-2:])     # last 2 char of str
print(my_name[-3:])     # lasr 3 char of str
print(my_name[0:5:2])   # every second char of str
print(my_name[:])       # all character
print(my_name[::])      # all character 
print(my_name[::-1])    # Reverse the string 

# String Methods 
word = "Hello, Madhav"

#1. len()
print(len(word))

#2. upper()
print(word.upper())

# 3. lower()
print(word.lower())

# 4. count()
print(word.count('a'))

# 5. find()
print(word.find('e'))

# 6. Split()
print(word.split(','))

# 7. Replace()
print(word.replace("Madhav", "Keshav"))

# 8. Title()
print(word.title())

# 9. Strip()
word2 = "  Hello World  "
print(word2.strip())

# 10. join()
zwords = ("Madhav", "is", "great")
print(" ".join(zwords))
print(",".join(words))
