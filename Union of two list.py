l1=[]
n1=int(input("Enter the length of first list:"))
for i in range(n1):
    c=int(input("Enter element"+str(i+1)+":"))
    l1.append(c)
print("The first list is:",l1)
l2=[]
n2=int(input("Enter the length of second list:"))
for j in range(n2):
    e=int(input("Enter element"+str(j+1)+":"))
    l2.append(e)
print("The second list is:",l2)
list=list(set().union(l1,l2))
print("The union of two list l1 and l2 is:",list)
