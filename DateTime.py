# # # # # from datetime import date
# # # # #
# # # # # # Create a date object
# # # # # today = date.today()
# # # # #
# # # # # # Print the current date
# # # # # print("Today's date:", today)  # Output: Today's date: YYYY-MM-DD
# # # # #
# # # # # # Creating a specific date
# # # # # birthday = date(1990, 5, 15)
# # # # #
# # # # # print("Birthday:", birthday)  # Output: Birthday: 1990-05-15
# # # # from datetime import datetime
# # # #
# # # # # Create a datetime object
# # # # now = datetime.now()
# # # #
# # # # # Print the current date and time
# # # # print("Current date and time:", now)  # Output: Current date and time: YYYY-MM-DD HH:MM:SS.ssssss
# # # #
# # # # # Creating a specific datetime
# # # # event = datetime(2024, 12, 25, 10, 0, 0)
# # # # print("Event datetime:", event)  # Output: Event datetime: 2024-12-25 10:00:00
# # # #
# # # from datetime import datetime, timedelta
# # # # Create two datetime objects
# # # start = datetime(2024, 1, 1)
# # # end = datetime(2024, 12, 31)
# # #
# # # # Calculate the difference between them
# # # delta = end - start
# # # print("Difference in days:", delta.days)  # Output: Difference in days: 364
# # #
# # # # Adding and subtracting time
# # # future_date = start + timedelta(days=30)
# # # print("Date after 30 days:", future_date)  # Output: Date after 30 days: 2024-01-31
# # from datetime import datetime
# # # Current datetime
# # now = datetime.now()
# #
# # # Formatting the datetime
# # formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# # print("Formatted date and time:", formatted_date)  # Output: Formatted date and time: YYYY-MM-DD HH:MM:SS
# #
# # # Custom formats
# # short_date = now.strftime("%d/%m/%Y")
# # print("Short date format:", short_date)  # Output: Short date format: DD/MM/YYYY
# #
# from datetime import datetime
# # Current datetime
# now = datetime.now()
#
# # Formatting the datetime
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted date and time:", formatted_date)  # Output: Formatted date and time: YYYY-MM-DD HH:MM:SS
#
# # Custom formats
# short_date = now.strftime("%d/%m/%Y")
# print("Short date format:", short_date)  # Output: Short date format: DD/MM/YYYY
#
# from datetime import datetime
#
# # Date string
# date_string = "25-12-2024 15:00"
#
# # Parsing the string into a datetime object
# parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
# print("Parsed datetime:", parsed_date)  # Output: Parsed datetime: 2024-12-25 15:00:00

# from datetime import date
#
# # Create a date object
# today = date.today()
#
# # Print the current date
# print("Today's date:", today)  # Output: Today's date: YYYY-MM-DD
#
# # Creating a specific date
# birthday = date(1990, 5, 15)
# print("Birthday:", birthday)  # Output: Birthday: 1990-05-15

# from datetime import time
#
# # Create a time object
# meeting_time = time(14, 30, 0)
#
# # Print the time
# print("Meeting time:", meeting_time)  # Output: Meeting time: 14:30:00
# hour = 12:30:30
# min = 30
# # Creating a specific time with milliseconds
# alarm_time = time(hour, min, 30, 500000)
# print("Alarm time:", alarm_time)  # Output: Alarm time: 07:45:30.500000

# from datetime import datetime
#
# # Create a datetime object
# now = datetime.now()
#
# # Print the current date and time
# print("Current date and time:", now)  # Output: Current date and time: YYYY-MM-DD HH:MM:SS.ssssss
#
# # Creating a specific datetime
# event = datetime(2024, 12, 25, 10, 0, 0)
# print("Event datetime:", event)  # Output: Event datetime: 2024-12-25 10:00:00

# from datetime import datetime, timedelta
# # Create two datetime objects
# start = datetime(1007, 12, 16)
# end = datetime(2024, 10, 7)
#
# # Calculate the difference between them
# delta = end - start
# print("Difference in days:", delta.days)  # Output: Difference in days: 364
#
# # Adding and subtracting time
# future_date = start + timedelta(days=30)
# print("Date after 30 days:", future_date)  # Output: Date after 30 days: 2024-01-31
#
# from datetime import datetime
# # Current datetime
# now = datetime.now()
#
# # Formatting the datetime
# formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
# print("Formatted date and time:", formatted_date)  # Output: Formatted date and time: YYYY-MM-DD HH:MM:SS
#
# # Custom formats
# short_date = now.strftime("%d/%m/%Y")
# print("Short date format:", short_date)  # Output: Short date format: DD/MM/YYYY

# from datetime import datetime
#
# # Date string
# date_string = "25-12-2024 15:00"
#
# # Parsing the string into a datetime object
# parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
# print("Parsed datetime:", parsed_date)  # Output: Parsed datetime: 2024-12-25 15:00:00

# import math
# print("Value of pi:", math.pi)
# print("Value of e:", math.e)
#
# #
# import math
#
# # Angle in radians
# angle = math.radians(45)
# print(angle)
# # Trigonometric functions
# sin_result = math.sin(angle)
# cos_result = math.cos(angle)
# tan_result = math.tan(angle)
#
# print("Sine of 45 degrees:", sin_result)
# print("Cosine of 45 degrees:", cos_result)
# print("Tangent of 45 degrees:", tan_result)


# import math
#
# # Rounding examples
# ceil_result = math.ceil(3.14)
# floor_result = math.floor(3.14)
# trunc_result = math.trunc(3.14)
#
# print("Ceiling of 3.14:", ceil_result)
# print("Floor of 3.14:", floor_result)
# print("Truncated value of 3.7:", trunc_result)

import math

def compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n)**(n*time)

print("Compound interest:", compound_interest(10000000, 0.05, 10, 12))

