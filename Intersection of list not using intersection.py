n1=int(input("Enter the length of first list:"))
l1=[]
for i in range(n1):
    c=int(input("Enter element"+str(i+1)+":"))
    l1.append(c)
print("The first list is:",l1)
n2=int(input("Enter the length of second list:"))
l2=[]
for j in range(n2):
    e=int(input("Enter element"+str(j+1)+":"))
    l2.append(e)
print("The second list is:",l2)
list=[]
def Common(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                if j in list:
                    pass
                else:
                    list.append(j)
    return list               
Common(l1,l2)
print("The intersection of two list:",list)
def Arrange(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
Arrange(list)
print("The arranged list is:",list)
            
