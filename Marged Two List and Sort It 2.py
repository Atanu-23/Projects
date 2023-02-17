n1=int(input("Enter length of first list:"))
list1=[]
for i in range(n1):
    e=int(input("Enter element %d:"%(i+1)))
    list1.append(e)
print("The first list is:",list1)
print("\n")
n2=int(input("Enter length of second list:"))
list2=[]
for j in range(n2):
    c=int(input("Enter element %d:"%(j+1)))
    list2.append(c)
print("The second list is:",list2)
print("\n")
list1.extend(list2)
print("The marged list is:",list1)
print("\n")
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print("The sorted marged list is:",list1)            
