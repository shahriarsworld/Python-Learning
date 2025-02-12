


# file = open("data2.txt", "r")
# # contents = file.read()
# # print(contents)
# line = file.readline()
# line2 = file.readline()
# print(line)
# print(line2)
# file.close()
#
# file = open("data2.txt", "w")
# file.write("Hello, World!")
# file.close()


import os
# Checking if a file exists
# file_path = "data2.txt"
# if os.path.exists(file_path):
#     print(f"The file '{file_path}' exists.")
# # Renaming a file
new_file_path = "renamed_data2.txt"
# os.rename(file_path, new_file_path)
# print(f"The file has been renamed to '{new_file_path}'.")
# # Deleting a file
os.remove(new_file_path)
print(f"The file '{new_file_path}' has been deleted.")

