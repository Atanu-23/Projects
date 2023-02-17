def SumofNestedlist(l):
    total=0
    for i in range(len(l)):
        if type(l[i])==list:
            total+=SumofNestedlist(l[i])
        else:
            total+=l[i]
    return total

n=int(input("Give number of list you want to enter:"))
list1=[]
list2=[]
print()
for j in range(1,n+1):
    m=int(input("Give nuber of element in list"+str(j)+":"))
    for k in range(1,m+1):
        e=int(input("Give element"+str(k)+":"))
        list1.append(e)
    list2.append(list1)
    list1=[]
a=int(input("Enter number of element:"))
for g in range(1,a+1):
    h=int(input("give element"+str(g)+":"))
    list2.append(h)
print("The list of list and element is:",list2)
print()
print("The sum of elements of flatten list is:",SumofNestedlist(list2))

