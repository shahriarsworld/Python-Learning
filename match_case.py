processor=input("what is the model of processor? Answer: ")

match processor:
    case "i5":
        print("Don't buy this.")
    case "ryzen":
        print("Buy this.")
    case _:
        print("error....")