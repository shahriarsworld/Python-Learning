def decorator(func):
    def wrapper():
        print("Transaction Started")
        func()
        print("Transaction Closed")
    return wrapper

@decorator
def transaction():
    balance = 50000
    cash = int(input("Enter your amount to send: "))
    newBalance = balance - cash
    print(f"Your current balance is: {newBalance}")

transaction()
