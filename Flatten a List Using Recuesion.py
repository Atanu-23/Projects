def Flattenlist(Nestedlist):
    if not(bool(Nestedlist)):
        return Nestedlist
    if isinstance(Nestedlist[0],list):
        return Flattenlist(*Nestedlist[:1])+Flattenlist(Nestedlist[1:])
    return Nestedlist[:1]+Flattenlist(Nestedlist[1:])

m=int(input("Enter number of list:"))
print()
list1=[]
list2=[]
for i in range(1,m+1):
    n=int(input("Enter length of list"+str(i)+":"))
    for j in range(0,n):
        e=int(input("Enter element"+str(j+1)+":"))
        list1.append(e)
    list2.append(list1)
    list1=[]
a=int(input("Enter number of element:"))
for g in range(1,a+1):
    h=int(input("give element"+str(g)+":"))
    list2.append(h)    
print("The list of list and element is:",list2)
print()
print("The list after flattening is:",Flattenlist(list2))
