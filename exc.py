# class Calculator:
#     @staticmethod
#     def add(x, y):
#         return x + y
#
# result = Calculator.add(5, 3)
# print("Result of addition:", result)  # Output: Result of addition: 8
#
# class Student:
#     total_students = 0  # Class variable to track total students
#
#     @classmethod
#     def count_students(cls):
#         print(f"Total students: {cls.total_students}")
#
# # Student.count_students()  # Output: Total students: 0
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Creating an instance of the Circle class
circle = Circle(radius=5)

# Calling the instance method
area = circle.calculate_area()
print("Area of the circle:", area)

