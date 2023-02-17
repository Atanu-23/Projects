n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    a=int(input("Enter element:"))
    l.append(a)
print("The list is:",l)
l.sort()
print("The new list is:",l)
print("The maximum element in the list is:",max(l))
