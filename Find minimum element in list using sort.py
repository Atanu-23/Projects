l=[]
n=int(input("Enter the range of list: "))
for i in range(n):
    a=int(input("Enter elements: "))
    l.append(a)
print(l)
l.sort()
print("After sorting the list is:",l)
print("The mininum element in the list is:",min(l))
