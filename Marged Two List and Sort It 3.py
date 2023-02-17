n1=int(input("Enter the length of first list:"))
list1=[]
for i in range(n1):
    c=int(input("Enter element"+str(i+1)+":"))
    list1.append(c)
print("The first list is:",list1)
print("\n")
n2=int(input("Enter the length of second list:"))
list2=[]
for j in range(n2):
    e=int(input("Enter element"+str(j+1)+":"))
    list2.append(e)
print("The second list is:",list2)
print("\n")
l=[*list1,*list2]
print("the marged list is:",l)
print('\n')
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The sorted marged list is:",l)

