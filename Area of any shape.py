# radius=float(input("Enter the radius of the circle = "))
# area=3.1416*radius*radius
# print(f"The area of the circle = {area}")


# r = float(input5.("Enter the radius of the circle = "))
# area = 3.1416*r*r
# print("area=",area)
def weekday(n):
   match n:
      case 0:
          return "Monday"
      case 1:
          return "Tuesday"
      case 2:
          return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
n=int(input("enter the number: "))
print(weekday(n))

# def access(user):
#    match user:
#       case "admin" | "manager": return "Full access"
#       case "Guest": return "Limited access"
#       case _: return "No access"
# print (access("manager"))
# print (access("Guest"))
# print (access("Ravi"))