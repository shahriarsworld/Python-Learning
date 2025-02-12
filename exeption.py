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
# else:
#     print(result)
# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
# except ValueError as er:
#     print(f"Error: {er}")
# try:
#     result = 10/e
#     print(result)
# # except ZeroDivisionError:
# #     print("it can't be divided by zero")
# except Exception as ex:
#     print(f"error: {ex}")
#
# try:
#   f = open("data")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
# try:
#     # Code that might raise an exception
#     file = open("dataa", "r")
#     # Process the file
#     try:
#         file.write("hello")
#     except FileNotFoundError:
#         print("File not found.")
#     finally:
#     # Close the file, regardless of exceptions
#         file.close()
# except:
#     print("something else is wrong check again")
# try:
#     password = input("Enter your password: ")
#     if len(password) < 8:
#         raise ValueError("Password is too short.")
#     print("Password accepted!")
# except ValueError as e:
#     print(f"Error: {e}")
# def safe_division(numerator, denominator):
#     try:
#         result = numerator / denominator
#         return result
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#
# # Example usage:
# num1 = float(input("Enter the numerator: "))
# num2 = float(input("Enter the denominator: "))
# print(f"Result: {safe_division(num1, num2)}")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")
