list1=[]
list2=[]
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for i in range(lower,upper+1):
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print("The even number list is:",list1)
print("The odd number list is:",list2)
