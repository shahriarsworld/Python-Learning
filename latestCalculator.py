num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operation: ")
match operator:
    case "+":
        print("Addition = ",num1+num2)
    case "-":
        print("Subtraction = ",num1-num2)
    case "*":
        print("Multiplication = ", num1*num2)
    case "/":
        print("Division = ", num1/num2)
    case _:
        print("error...")