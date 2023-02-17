l=[]
l1=[]
list1=[]
n=int(input("Enter the number of tuple in the list:"))
for i in range(1,n+1):
    m=int(input("Enter length of tuple"+str(i)+":"))
    for j in range(m):
        e=int(input("Enter elements"+str(j+1)+":"))
        l.append(e)
    t=tuple(l)    
    l1.append(t)
    l=[]
    t=()
print("The list is:",l1)
for t in l1:
    l2=list(t)
    for i in range(len(l2)):
        for j in range(i+1,len(l2)):
            if l2[i]>l2[j]:
                l2[i],l2[j]=l2[j],l2[i]
    t1=tuple(l2)       
    list1.append(t1)
    l2=[]
    t1=()
print("The arranged number tuple of list is:")
print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i][-1]>list1[j][-1]:
            list1[i],list1[j]=list1[j],list1[i]
print("The list of arranged number tuple according to last element is:")
print(list1)
