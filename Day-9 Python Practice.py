# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Method Overriding
# Problem Statement : Create a class Animal with a method sound() that prints "Animal makes a sound". Create a class Cat that inherits from Animal and overrides the sound() method to print "Cat says Meow". Create an object of the Cat class and call the sound() method.
# Example Output - Cat says Meow
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
cat = Cat()
cat.sound()

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Polymorphism
# Problem Statement : Create two classes: Dog with a method speak() that prints "Dog barks". Cow with a method speak() that prints "Cow moos".
# Create a function make_sound(animal) that calls the speak() method of the object passed to it.
# Example Output : Dog barks, Cow moos
class Dog:
    def speak(self):
        print("Dog barks")
class Cow:
    def speak(self):
        print("Cow moos")
def make_sound(animal):
    animal.speak()
dog = Dog()
cow = Cow()
make_sound(dog)
make_sound(cow)
