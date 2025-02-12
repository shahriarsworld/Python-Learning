for i in range(15):
    if (i==10):
        break
    print("5 x ",i+1,"=",5*(i+1))

for j in [2,4,6,7,8,10]:
    if (j%2!=0):
        continue
    print(j)