list=[]
count=a=0
x=int(input("Enter the elements which we want to find in list:"))
n=int(input("Enter the length of list:"))
for i in range(n):
    a=int(input("Enter the element:"))
    list.append(a)
print("The list is:",list)
for i in list:
    if x==i:
        count=count+1
    a=i    
if x==a:
    print("Element found")
    print("The element which is repeated is:",x)
    print("{} has repeated {} times".format(x,count))
else:
    print("Element not found")
