n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    a=int(input("Enter element %d:"%(i+1)))
    l.append(a)
print("The list is:",l)
l.sort()
print("The new list is:",l)
       
print("Second maximum number in list is:",l[-2])
print("Second minimum number in list is:",l[1])
