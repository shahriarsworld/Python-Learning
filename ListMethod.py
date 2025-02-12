list=[4,6,2,8,1,9,13,20,10,1,17,1]
list2=[50,60,70,80,90]
print(list)
list.append(30)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(f"The given number is used {list.count(100)} times")
list.insert(0,100)
print(list)
list.extend(list2)
print(list)
nums=(input("Enter numbers in the list: "))
list3= nums.split()
sum=0
for i in list3:
    sum=sum+int(i)
print(sum)
print(list3)
