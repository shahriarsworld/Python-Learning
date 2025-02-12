print("-----Tour Plan-----")
friends=input("Are my friends going? Answer: ")

if (friends=="yes"):
    print("Yes! We are going on a tour!")
    tour=input("Where are we going? Answer: ")
    if (tour=="kaptai"):
        print("Okay We are going to Kaptai")
    elif (tour=="cox"):
        print("Okay We are going to Cox")
    else:
        print("sorry it is not an option")

elif (friends=="no"):
    print("Oh no! we are not going this time")

else:
    print("error")
