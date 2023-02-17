n=int(input("Enter length of list:"))
l=[]
for i in range(n):
    a=int(input("Enter element %d:"%(i+1)))
    l.append(a)
print("The list is:",l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The new list is:",l)

first_max=second_max=0
def Find_Second_max(l):
    first_max=max(l[0],l[1])
    second_max=min(l[0],l[1])
    for i in range(2,len(l)):
        if l[i]>first_max:
            second_max=first_max
            first_max=l[i]
        elif l[i]>second_max and first_max!=l[i]:
            second_max=l[i]
            
    print("The second maximum is:",second_max)
Find_Second_max(l)    

first_min=second_min=0
def Find_Second_min(l):
    first_min=min(l[0],l[1])
    second_min=max(l[0],l[1])
    for i in range(2,len(l)):
        if l[i]<first_min:
            second_min=first_min
            first_min=l[i]
        elif l[i]<second_min and first_min!=l[i]:
            second_min=l[i]
            
    print("The second minimum is:",second_min)
Find_Second_min(l)   


