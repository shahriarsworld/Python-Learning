# class Person:
#     age = 0
#     name = ""
#
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
#
#     def showInfo(self):
#         print(f"my name is {self.name} and my age is {self.age}")
#
#     @classmethod
#     def changeAge(cls,age):
#         cls.age = age
# Person.changeAge(12)
# print(Person.age)
# p1 = Person(18,"Sayem")
# p1.showInfo()
#
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Afif', 21)
person2 = Person.fromBirthYear('Afif', 1996)

print(person1.age)
print(person2.age)
print(date.today())
# print the result
print(Person.isAdult(22))