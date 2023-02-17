n1=int(input("Enter the range of first list:"))
l1=[]
for i in range(n1):
    c=int(input("Enter element"+str(i+1)+":"))
    l1.append(c)
print("The first list is:",l1)
n2=int(input("Enter the range of second list:"))
l2=[]
for j in range(n2):
    e=int(input("Enter element"+str(j+1)+":"))
    l2.append(e)
print("The second list is:",l2)
list=list(set.intersection(set(l1),set(l2)))
print("The intersection of two list is:",list)
