# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
# # Creating an instance of the Circle class
# circle = Circle(radius=6)
# # Calling the instance method
# area = circle.calculate_area()
# print("Area of the circle:", area)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def showName(self):
#         print(f"The name is {self.name} and the age is {self.age}")
#
# # Creating an instance of the Person class using the constructor
# person1 = Person("alice",22)
# person1.showName()
# person2 = Person("Wasia",20)
# person2.showName()
#
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog barks")
#
# # Creating objects
# my_dog = Dog()
# my_dog.speak()  # Output: Animal speaks
# my_dog.bark()   # Output: Dog barks

# class Parent:
#     def show(self):
#         print("Parent method")
#
# class Child(Parent):
#     def show(self):  # Method overriding
#         print("Child method")
#
# # Creating object
# child = Child()
# child.show()  # Output: Child method

def add(num1, num2):
    print(num1 + num2)

num1= int(input("enter num1= "))
num2= int(input("enter num2= "))
add(num1,num2)

