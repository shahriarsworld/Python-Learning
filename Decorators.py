# def log_args_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", args)
#         print("Keyword arguments:", kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_args_decorator
# def greet(name, age):
#     print(f"Hello, {name}! You are {age} years old.")
#
# greet("Alice", age=30)
def decorator(func):
 def wrapper():
   print("Transaction Started")
   func()
   print("Transaction Closed")
 return wrapper

@decorator
def transaction():
   balance = 50000
   cash = int(input("Enter your amount to send: "))
   newBalance = balance - cash
   print(f"Your current balance is: {newBalance}")

transaction()

# def my_decorator(func):
#     def wrapper():
#         print("Before function call- good morning")
#         func()
#         print("After function call- goodbye")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello, world!")
#     print("2+2=4")
#
# say_hello()  # Output: Before function call, Hello, world!, After function call
#
# def greet_decorator(func):
#     def wrapper():
#         print("Hello!")
#         func()
#         print("Goodbye!")
#     return wrapper
#
# @greet_decorator
# def say_name():
#     print("John")
#
# say_name()  # Output: Hello! John Goodbye!

# def weddingHall(func):
#     def wrapper():
#         print("welcome to the wedding")
#         func()
#         print("Biya shesh khoda hafez")
#     return wrapper()
# @weddingHall
# def name():
#     print("my name is OG")
#
# name()

# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
# def exclamation_decorator(func):
#     def wrapper():
#         result = func()
#         return result + "!"
#     return wrapper
#
# @uppercase_decorator
# @exclamation_decorator
# def say_hello():
#     return "hello wasi and nirob"
# print(say_hello())  # Output: HELLO!

# def authenticate(func):
#     def wrapper(username, password):
#         if username == "admin" and password == "password":
#             return func()
#         else:
#             return "Access denied"
#     return wrapper
#
# @authenticate
# def protected_function():
#     return "Access granted"
#
# print(protected_function("admin", "password"))

# def log_args_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", args)
#         print("Keyword arguments:", kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_args_decorator
# def greet(name, age):
#     print(f"Hello, {name}! You are {age} years old.")
#
# greet("Alice", age=30)

