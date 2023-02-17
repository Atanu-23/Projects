n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    q=int(input("Enter element:"))
    l.append(q)
print("The list is:",l)
min=l[0]
def Minimum(min,l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>=l[j]:
                l[i],l[j]=l[j],l[i]

    print("The new list is:",l)
    for i in range(n):
        if l[i]<min:
            min=l[i]
    print("The minimum element in list is:",min)
Minimum(min,l)        
            
