num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter your operator: ")
if (operator=='+'):
    print("Summation = ",num1+num2)
elif (operator=='-'):
    print("Subtraction = ",num1-num2)
elif (operator=='*'):
    print("Multiplication = ",num1*num2)
elif (operator=='/'):
    print("Division = ",num1/num2)
else:
    print("Invalid Operator")