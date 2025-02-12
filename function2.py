# # def fullnamegenerator(name1,name2):
# #     fname= name1
# #     lname= name2
# #     fullname=fname+lname
# #     print(fullname)
# # first=input("First Name: ")
# # last=input("Last Name: ")
# # fullnamegenerator("Symuddin ")
# # fullnamegenerator("Shahriar ","Shihab")
# #
# # def name(fname, mname = "", lname = "Parker"):
# #     print("Hello,", fname, mname, lname)
# # name("Peter","johnson","Wasi")
# def name(*name):
#     print("Hello,", name[0], name[1], name[2],name[3])
#
# name("Spiderman", "Ironman", "Batman","Superman")
#
# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])
#
# name(mname = "Rogers", lname = "Captain America", fname = "Steve")
# def my_function(x):
#   return 5 * x
# #
# # print(my_function(3))
# # print(my_function(5))
# # print(my_function(9))
# def my_function(food):
#   print(food)
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

# def info(name):
#   pass
# info("asif")
# import math
# #
# # def compound_interest(principal, rate, time, n):
# #     return principal * (1 + rate/n)**(n*time)
# #
# # print("Compound interest:", compound_interest(1000, 0.05, 10, 12))
# # Traditional Function
# def add(x, y):
#     return x + y
#
# # Equivalent Lambda Function
# add_lambda = lambda x, y,z: x * y +z
#
# print(add(3,5))
# result = add_lambda(3, 5, 2)
# print(result)  # Output: 8
# value=input("enter a value: ")
# match value:
#     case "1":
#         print("Value is 1")
#     case "hello":
#         print("Value is 'hello'")
#     case _:
#         print("Value doesn't match any specific pattern")
#
# match value:
#     case "1":
#         print("hello")
#         print("hello")
#         print("hello")
#         print("hello")
#         print("hello")
#         print("hello")
#     case "2":
#         c=3
#         b=5
#         print(c+b)
# #     case _:
# #         print("invalid input")
# dice_roll = input("enter the value: ")
#
# match dice_roll:
#     case "1":
#         print("You rolled a one!")
#     case "6":
#         print("You rolled a six!")
# #     case _:
# #         print("You rolled a standard value")
#
# def weekday(n):
#  match n:
#   case 0: return "Monday"
#   case 1: return "Tuesday"
#   case 2: return "Wednesday"
#   case 3: return "Thursday"
#   case 4: return "Friday"
#   case 5: return "Saturday"
#   case 6: return "Sunday"
#   case _: return "Invalid day number"
# print (weekday(3))
# print (weekday(6))
# print (weekday(7))
def access(user):
 match user:
  case "admin" | "manager": return "Full access"
  case "Guest": return "Limited access"
  case _: return "No access"
print (access("manager"))
print (access("admin"))
print (access("Guest"))
print (access("Ravi"))


