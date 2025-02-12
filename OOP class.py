class Vehicle:
    pass
class Car:
    brand = ""
    model = ""
    speed = 0

    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def carInfo(self):
        print(f"I have a {self.brand} car and the model is {self.model}.")
        print(f"The top speed is {self.speed} kmph")
    def checkPost(self):
        if self.speed >= 70:
            print("You have to pay 1000tk as a fine")
        else:
            print("you're good to go")

# car1 = Car()
# car1.brand = "BMW"
# car1.model = "M3 GTR"
# car1.speed = 80
# car1.carInfo()
# car1.checkPost()
# car2 = Car()
# car2.brand = "Toyota"
# car2.model = "Corolla"
# car2.speed = 50
# car2.carInfo()
# # car2.checkPost()
# car3 = Car("Lamborghini","Hurracan",100)
# car3.carInfo()
# car3.checkPost()
car4= SportsCar()