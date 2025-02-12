# username = input("Enter your username: ")
# if username == "admin":
#     password = input("Enter your password: ")
#     if password == "synthwave":
#         print("Login successful!")
#     else:
#         print("Incorrect password.")
# else:
# #     print("Unknown username.")
# num = int(input("Enter a number: "))
# factorial = 1
# while num > 0:
#          factorial *= num
#          num -= 1
# print(f"The factorial is: {factorial}")
# while True:
# #     user_input = input("Enter a number ('skip' to skip, 'exit' to stop): ")
# #     if user_input.lower() == 'exit':
# #         break
# #     elif user_input.lower() == 'skip':
# #         continue
#     else:
# #         print(f"You entered: {user_input}")
# correct_password = "password123"
# attempts_left = 3

# while attempts_left > 0:
#     user_password = input(f"Enter the password ({attempts_left} attempts left): ")
#     if user_password == correct_password:
#         print("Password correct. Access granted!")
#         break
#     else:
#         print("Incorrect password. Try again.")
#         attempts_left -= 1
#
# if attempts_left == 0:
#     print("Out of attempts. Exiting.")
# Get the number for which the multiplication table is needed
# number = int(input("Enter a number for the multiplication table: "))

# Print the multiplication table using a for loop
# print(f"Multiplication table for {number}:")
#
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
# price = 190
# discount = 0.15
# final_price = f"The discounted price is tk {price - (price * discount):.2f}."
# print(final_price)
# Example Program: Indexing and slicing
# shopping_list = ["oranges","apples",1,"mango","banana","pineapple"]
# print("Subset of the shopping list:", shopping_list[1:5:1])
# copied= shopping_list.copy()
# cop=shopping_list[:]
# print(copied)
# print(cop)
# user_input = input("Enter items separated by spaces: ")
# user_list = int(user_input.split())
# print("Your items:", user_list)

# price = 190
# discount = 39.999
# final_price = f"The discounted price is tk {price - (price * discount):.5f}"
# print(final_price)
# count = 3
# while count <= 10:
#     print(count)
#     count += 3
# for num in range(1,21):
# #     print(num,"yes")
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# total = 0
# for num in range(start, end + 1):
#     total = num + total
#     print(f"The sum is: {total}")
for num in range(1, 101):
    if num % 2 == 0:
        continue
    print(num)


