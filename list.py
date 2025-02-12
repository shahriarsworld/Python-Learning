# shopping_list=["moyda","Alu","Bread","Oil","Alu"]
# print(shopping_list)
# item1= shopping_list[0]
# print(item1)
# print("My name is Z")
# item3=shopping_list[2]
# print(item3)
# shopping_list[0]="atta"
# print(shopping_list)
# # del shopping_list[3]
# # print(shopping_list)
# shortList=shopping_list[1:3]
# print(shortList)
# copiedList= shopping_list[:]
# del copiedList[1]
# print(copiedList)
# print(shopping_list)
# # Example Program: Using list methods
# shopping_list.append("milk")# Append "milk" to the end
# print(shopping_list)
# oranges_count = shopping_list.count("Alu")# Count occurrences of "oranges"
# print(oranges_count)
# index_of_cheese = shopping_list.index("Bread")# Find the index of "cheese"
# print(index_of_cheese)
# shopping_list.insert(1, "cookies") # Insert "cookies" at index 1
# print(shopping_list)
# user_input = input("Enter items separated by spaces: ")
# if user_input:
#     user_list = user_input.split()
#     print("Your items:", user_list)
# else:
#     print("No items entered. Please try again.")
# Example Program: Taking user input inside a list
user_items = []
num_items = int(input("Enter the number of items you want to add: "))
for i in range(num_items):
    item = input(f"Enter item {i + 1}: ")
    user_items.append(item)
print("Your items:", user_items)
