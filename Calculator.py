#this two line takes input from user
number=2
def calc():
    number2 = 3
    thanks = "Thank you for using my Calculator"
    welcome = "Welcome to my Calculator Program"
    print(welcome.center(50, ("-")))
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))
    # this four lines prints output
    print("Addition = ", int(num1 + num2))
    print("Subtraction = ", num1 - num2)
    print("Multiplication = ", num1 * num2)
    print("Division = ", num1 / num2)
    print("Exponential = ", num1 ** num2)
    print(thanks.center(50, ("-")))
