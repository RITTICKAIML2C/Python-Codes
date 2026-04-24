# OOPS in Python
# OOP - Object Oriented Programming 

# Using List - creating student records
# students details 
student_1 = ['Madhav', 10] # Name, Grade
student_2 = ['Vishakha', 12]
student_3 = 'Keshav'

student_1.append('A')
print(student_1)
print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')


# using OOPs - creating student records 

# class - blueprint or template
# __init__ method - constructor, value initialize - fixed
# self parameter - reference or connection build between class and object
class Student: # student class
    def __init__(self, name, grade, percentage): # method 
        self.name = name # attribute
        self.grade = grade # attribute
        self.percentage = percentage # attribute

    def student_details(self): # method
        print(f"{self.name} is in Class {self.grade}, with {self.percentage}%")

# Object - instance of class
student1 = Student('Madhav', 11, 96)
print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
print(student2.name, student2.grade)

print(student1.percentage)
student1.student_details()
student2.student_details()

print(student1.__dict__) # gets converted into dictionary

# Modfiy object property
print(student1.percentage)
student1.percentage = 98 # modify 
print(student1.percentage)

# Delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)

# delete object 
del student1
print(student1) # error



# class - blueprint or template
class Student: # student class
    def __init__(self, name, grade, percentage, team): # method 
        self.name = name # attribute
        self.grade = grade # attribute
        self.percentage = percentage # attribute
        self.team = team # attribute
    def student_details(self): # method
        print(f"{self.name} is in Class {self.grade}, with {self.percentage}% and is in team {self.team}")

team1 = 'A'
team2 = 'B'

# Object - instance of class
student1 = Student('Madhav', 11, 96, team1)
print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99, team2)
print(student2.name, student2.grade)

print(student2.team)
student1.student_details()
student2.student_details()


# 4 Features in OOPs
# Abstraction
# Encapsulation
# Inheritance 
# Polymorphism

# 1. Abstraction -
# hiding unnecessary details from users through class, methods
class Student: # student class
    def __init__(self, name, grade, percentage):
        self.name = name # attribute
        self.grade = grade 
        self.percentage = percentage

    def student_details(self): # method - abstraction
        print(f"{self.name} is in class {self.grade}, with {self.percentage+2}%") # hidden from users

object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

student1.student_details()


# 2. Encapsulation - 
# Restrict access to certain attributes or methods to protect data and enforce controlled access

class Student: # student class
    def __init__(self, name, grade, percentage):
        self.name = name # attribute
        self.grade = grade 
        self.__percentage = percentage  # double underscore (__) linits access

    def get_percentage(self):
        return self.__percentage

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

print(student1.__percentage)  # error
print(student1.percentage)  # error
print(student1.get_percentage())
print(student2.get_percentage())


# 3. Inheritance - 
# allows one class (child) to reuse the properties and methods of another class (parents).

# parent class - baap
class Student: # student class
    def __init__(self, name, grade, percentage):
        self.name = name # attribute
        self.grade = grade 
        self.percentage = percentage

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

student1.student_details()

child class - beta
class GraduateStudent(Student): # GraduateStudent a child class which inherits prop and methods from Student Parent class
    def __init__(self, name, grade, percentage, stream): # old parameters from parent class and new parameters in child class.
        super().__init__(name, grade, percentage) # super - call parent class init
        self.stream = stream # new attribute in child class

    def student_detials(self):
        super().student_details() # method inherit from parent class
        print(f'Stream is {self.stream}')

# Object 
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')
print(Grad_Student1.stream)

Grad_Student1.student_details()


# 4. Polymorphism - 
# allows method in different classes to have same name but different behaviour depending on objects

class Student: # student class
    def __init__(self, name, grade, percentage):
        self.name = name # attribute
        self.grade = grade 
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%") 

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 99)

# child class - beta 
class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage)
        self.stream = stream

    def student_details(self): # method
        # print(f'{self.name} is in class {self.grade}, with {self.percentage}% and from Stream {self.stream}')
        print('same method with diff o/p ')
# object - student class
student1 = Student('Madhav', 11, 96)

# object - GraduateStudent class
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')

student1.student_details()
Grad_Student1.student_details()
