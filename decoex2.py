# def greet(func):
#     def wrapper():
#         print("good evening")
#         func()
#         print("thank you for using the app")
#     return wrapper
# @greet
# def hello():
#     print("Welcome back bro")
#     print("don't lose hope. You're doing great.")
#
# hello()
#
#
# # def make_pretty(func):
# #
# #     def inner():
# #         print("I got decorated")
# #         func()
# #     return inner
# #
# # @make_pretty
# # def ordinary():
# #     print("I am ordinary")
# # ordinary()
def greet(func):
    def wrapper():
        print("Welcome to our App")
        func()
        print("Good bye everything will be alright")
    return wrapper
@greet
def motivate():
    print("You're doing great - Safia")
    print("Don't give up - Samia")
motivate()