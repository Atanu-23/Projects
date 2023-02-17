n=int(input("Enter the length of list:"))
l=[]
for i in range(0,n):
    b=input("Enter element"+str(i+1)+":")
    l.append(b)
print("The list is:",l)
print("\n")
l.sort(key=len)
print("The sorted list according to the length of element is:",l)
