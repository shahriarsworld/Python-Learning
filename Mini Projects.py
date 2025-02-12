#task1
import time

# def stopwatch():
#
#     input("Press Enter to start the stopwatch")
#     start_time = time.time()
#     input("Press Enter to stop the stopwatch")
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.2f} seconds")
#
# stopwatch()
# #
# #task2
import time

def reminder_app(reminder, interval):
    while True:
        print(reminder)
        time.sleep(interval)

def set_reminder():
    reminder = input("Enter reminder message: ")
    interval = int(input("Enter interval in seconds: "))
    reminder_app(reminder, interval)

set_reminder()
#
# def contact_manager():
#     contacts = {}
#
#     while True:
#         action = input("Choose an action: add, view, remove, or quit: ").strip().lower()
#
#         if action == "add":
#             name = input("Enter name: ")
#             phone = input("Enter phone number: ")
#             contacts[name] = phone
#             print(f"Added {name} with phone number {phone}")
#
#         elif action == "view":
#             if contacts:
#                 for name, phone in contacts.items():
#                     print(f"{name}: {phone}")
#             else:
#                 print("No contacts found.")
#
#         elif action == "remove":
#             name = input("Enter name to remove: ")
#             if name in contacts:
#                 del contacts[name]
#                 print(f"Removed {name}")
#             else:
#                 print("Contact not found.")
#
#         elif action == "quit":
#             break
#         else:
#             print("Invalid action. Please try again.")
#
# contact_manager()
