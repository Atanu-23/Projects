import operator
n1=int(input("Enter the length of first list:"))
list1=[]
for i in range(n1):
    e=int(input("Enter element %d:"%(i+1)))
    list1.append(e)
print("The first list is:",list1)
print("\n")
n2=int(input("Enter the length of second list:"))
list2=[]
for j in range(n2):
    c=int(input("Enter element %d:"%(j+1)))
    list2.append(c)
print("The second list is:",list2)
print("\n")
l=operator.add(list1,list2)
print("The marged list is:",l)
print("\n")
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The sorted merged list is:",l)        
