# import Calculator
# Calculator.calc()
import random
random_number = random.randint(1, 100)
attempts = 0
while True:
 guess = int(input("Guess the number (between 1 and 100): "))
 attempts += 1
 if guess == random_number:
   print(f"Congratulations! You guessed the number in {attempts} attempts.")
   break
 elif guess < random_number:
   print("Try higher.")
 else:
   print("Try lower.")

