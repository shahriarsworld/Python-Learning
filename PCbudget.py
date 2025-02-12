budget=int(input("Enter your budget: "))
choice=int(input("Your favourite PC price: "))
if (choice<=budget):
    print("Good. Buy this.")
    if (choice<=20000):
        print("very good")
    else:
        print("Not bad")
else:
    print("No. Don't buy this")