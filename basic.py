# from packDemo import addition,greet
# greet.greetings()
# print(addition.add(5,6))
# import packDemo
# from basic2.reverse import rev
# from basic2.capital import cap
#
# rev("Nirob is a good student")
# cap("my name is Wasi. he is from CCPC")

# def test():
#     pass
#
# # print("hi")
# try:
#     # Code that might raise an exception
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     # Handling a specific exception (invalid input)
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     # Handling a specific exception (division by zero)
#     print("Division by zero is not allowed.")

# try:
#     # Code that might raise an exception
#     result = 10 / gghggh
#
# except Exception as e:
#     # Handling any exception
#     print(f"An error occurred which is also a crime: {e}")

# try:
#     # Code that might raise an exception
#     result = 10 / 5
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# else:
#     print(f"Result: {result}")
#     result=result+5
#     print("hello")



try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative it must be positive.")
except ValueError as e:
    print(f"Error: {e}")


