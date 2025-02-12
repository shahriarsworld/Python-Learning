print("--------QUIZ GAME--------")
ques=[
    "1)How many consonants are there in the English alphabet?",
    "2)Baby frog is known as.....",
    "3)How many seconds make one hour?"
]
ans=[
    "21",
    "Tadpole",
    "3600"
]
point=0
print(ques[0])
print("a)25    b)24    c)21    d)20")
ans1=input("Enter your answer: ")
if (ans1==ans[0] or 'c'):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer.")
print("--------------------")
print(ques[1])
print("a)Tadpole   b)Cub    c)Lamb    d)Kitten")
ans2=input("Enter your answer: ")
if (ans2==ans[1] or 'a'):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer. You got no points")
print("--------------------")
print(ques[2])
print("a)3600   b)3800    c)4200    d)4000")
ans3=input("Enter your answer: ")
if (ans3==ans[2] or 'a'):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer.")
print("--------------------")
print(f"Your total Score is {point} out of 15")