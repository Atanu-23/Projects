m=int(input("Enter number of list:"))
list1=[]
list2=[]
for i in range(1,m+1):
    n=int(input("Give length of list"+str(i)+":"))
    for j in range(1,n+1):
        e=int(input("Enter element"+str(j)+":"))
        list1.append(e)
    list2.append(list1)
    list1=[]
print("List of list is:",list2)
print()

def SumofElementofList(l):
    total=0

    for k in range(len(l)):

        if type(l[k])==list:
            total+=SumofElementofList(l[k])

        else:
            total+=l[k]

    return total
print("Sum of all element in the list is:",SumofElementofList(list2))    
