def isBigger (a,b):
    if (a>b):
        print(a," is bigger")
    else:
        print(b," is bigger")
def print1to100():
    for i in range(1,101):
        print(i,end=" ,")
print("1. Check which Bigger")
print("2. Print 1 to 100")
print("3. Exit Program")
while True:
 choice=input("\nEnter your choice: ")
 match choice:
    case '1':
        c=int(input("Enter first number: "))
        d=int(input("Enter second number: "))
        isBigger(c,d)
    case '2':
        print1to100()
    case '3':
        print("Exiting Program...")
        break
    case _:
        print("Invalid Selection")