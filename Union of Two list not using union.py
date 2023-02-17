n1=int(input("Enter the length of first list:"))
list1=[]
for i in range(n1):
    c=int(input("Enter element"+str(i+1)+":"))
    list1.append(c)
print("The first list is:",list1)
n2=int(input("Enter the length of second list:"))
list2=[]
for j in range(n2):
    e=int(input("Enter element"+str(j+1)+":"))
    list2.append(e)
print("The second list is:",list2)
list=[]

def No_Duplicate(list1,list2):
    for element in list1:
        if element not in list:
            list.append(element)
    for element in list2:
        if element not in list:
            list.append(element)
    return list
No_Duplicate(list1,list2)
print("The union of list is:",list)
def Arrange(data):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
Arrange(list)
print("The arranged list is:",list)
