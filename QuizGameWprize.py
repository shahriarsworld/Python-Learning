print("--------QUIZ GAME--------")
ques=[
    "1)How many consonants are there in the English alphabet?",
    "2)Baby frog is known as.....",
    "3)How many seconds make one hour?"
]
ans=[
    "3600","tadpole",
    "21",
    "c","a","a"
]
point=0
print(ques[0])
print("a)25   b)24    c)21    d)20")
ans1=input("Enter your answer: ").lower()
if (ans1==ans[0]) or (ans1==ans[3]):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer. You got no points")
print("--------------------")
print(ques[1])
print("a)Tadpole   b)Cub    c)Lamb    d)Kitten")
ans2=input("Enter your answer: ").lower()
if (ans2==ans[1]) or (ans2==ans[4]):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer. You got no points")
print("--------------------")
print(ques[2])
print("a)3600   b)3800    c)4200    d)4000")
ans3=input("Enter your answer: ").lower()
if (ans3==ans[2]) or (ans3==ans[5]):
    print("Correct answer!")
    point=point+5
    print(f"Current Score = {point}")
else:
    print("Wrong answer. You got no points")
print("--------------------")
print(f"Your total Score is {point} out of 15")

