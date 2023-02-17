n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    a=int(input("Enter element:"))
    l.append(a)
print("The list is:",l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The new list is:",l)            
l.remove(max(l))
l.remove(min(l))
s_max=max(l)
s_min=min(l)
print("Second maximum number in the list is:",s_max)
print("Second minimum number in the list is:",s_min)
    
