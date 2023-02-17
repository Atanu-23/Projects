m=int(input("Enter the number of tuple in list:"))
l=[]
list=[]
list1=[]
for i in range(1,m+1):
    n=int(input("Enter length of list"+str(i)+":"))
    for j in range(n):
        e=int(input("Enter element"+str(j+1)+":"))
        list.append(e)
    t=tuple(list)    
    list1.append(t)
    list=[]
    t=()
print("The original List of tuple is:",list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i][-1]>list1[j][-1]:
            list1[i],list1[j]=list1[j],list1[i]
print("The list of tuple in sorted order by last element is:",list1)                
   
