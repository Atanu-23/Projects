m=int(input("Enter number of list:"))
list=[]
list1=[]
for i in range(1,m+1):
    n=int(input("Enter length of list"+str(i+1)+":"))
    for j in range(0,n):
        e=int(input("Enter element"+str(j+1)+":"))
        list.append(e)
    list1.append(tuple(list))
    list=[]
print(list1)    
