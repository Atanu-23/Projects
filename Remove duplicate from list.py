n=int(input("Enter length of list:"))
list=[]
list1=[]
for i in range(1,n+1):
    e=int(input("Enter element"+str(i)+":"))
    list.append(e)
print("The list is:",list)
print("\n")
def Remove_Duplicate(list,list1):
    
    for item in list:
        if item not in list1:
            list1.append(item)
    return list1
Remove_Duplicate(list,list1)
print("The list without duplicate element is:",list1)
print("\n")
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print("The arranged list without duplicate element is:",list1)             
