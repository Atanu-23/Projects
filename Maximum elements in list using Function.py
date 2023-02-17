n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    q=int(input("Enter element:"))
    l.append(q)
print("The list is:",l)
max=l[0]
def Maximum(max,l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>=l[j]:
               l[i],l[j]=l[j],l[i]
               
    print("The new list is:",l)        
    for i in range(n):
        if l[i]>max:
            max=l[i]
    print("The maximum element in list is:",max)
Maximum(max,l)    
        
    
