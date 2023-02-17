m=int(input("Enter number of tuple want to enter in list:"))
list=[]
list1=[]
for i in range(1,m+1):
    e=int(input("Enter element"+str(i)+":"))
    list.append(e)
    list.append(e*e)
    list1.append(tuple(list))
    list=[]
print("The list of tuple of number and it's square is:")
print()
print(list1)
    
