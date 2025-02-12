import random

while True:
    print("1. Roll the dice   2. Exit")
    user = int(input("What do you want to do? : "))
    if user == 1:
        number = random.randint(1, 6)
        print(number)
        if number == 1 or number == 6:
            print("Congrats! You got the lucky number!")

    elif user == 2:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1 to roll the dice or 2 to exit.")
