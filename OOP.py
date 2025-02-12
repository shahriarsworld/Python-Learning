class Car:
    brand = ""
    model = ""
    speed = 0

    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed


    def carInfo(self):
      print(f"I have a {self.brand} car and the model is {self.model} ")
      print(f"The top speed is {self.speed}mph")
    def checkPost(self):
      if self.speed <=150:
        print("You're good to go")
      else:
        print("You have to pay 1000tk for over speeding in Karnaphuly Tunnel")
class Bike:
    brand = ""
    model = ""
    speed = 0
    def bikeInfo(self):
        print(f"brand {self.brand}, model {self.model}")

# car1=Car()
# car1.brand = "BMW"
# car1.model = "M3 GTR"
# car1.speed = 200
# car1.carInfo()
# car1.checkPost()

# bike1=Bike()
# bike1.brand = "Yamaha"
# bike1.model = "R15"
# bike1.bikeInfo()

car2 = Car("Audi","RS7",250)
car2.carInfo()
car2.checkPost()

