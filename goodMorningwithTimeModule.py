import time
timestamp=time.strftime('%H:%M:%S')
print("The time right now is ",timestamp)
if int(time.strftime('%H'))> 5 and int(time.strftime('%H'))<12:
    print("Good Morning, Sir")
else:
    print("Good Evening, Sir")
