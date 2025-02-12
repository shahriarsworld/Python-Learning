def ifBigger(a,b):
    if (a>b):
       print(a," is bigger than ",b)
    else:
        print(b, " is bigger than ", a)
def oneTo100():
    for i in range(1,101):
        print(i,end=",")
print("-----MENU-----")
print("1) Check which number is bigger")
print("2) Print 1 to 100")
print("3) Exit Program")
while True:
    choice=int(input("\nEnter your choice: "))
    match choice:
        case 1 :
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
            ifBigger(num1,num2)
        case 2:
            oneTo100()
        case 3:
            print("Exiting Program....")
            break
        case _:
            print("Please select a valid option")



