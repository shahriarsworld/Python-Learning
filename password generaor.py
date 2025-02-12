import random


passlen = int(input("Enter the length of the password: "))


characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(characters, passlen))
print("Generated Password:", password)

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
# num1 = float(input("Enter the numerator: "))
# num2 = float(input("Enter the denominator: "))
# print(f"Result: {safe_division(num1, num2)}")


