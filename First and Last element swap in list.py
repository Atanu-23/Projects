n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    e=int(input("Enter element"+str(i+1)+":"))
    l.append(e)
print("The list is:",l)
print("\n")
l[0],l[-1]=l[-1],l[0]
print("The list after swapping first and last elements is:",l)
print("\n")
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The sorted list after swapping first and last elements is:",l)
print("\n")
l[0],l[-1]=l[-1],l[0]
print("The list after swapping first and last element in the sorted list is:",l)
