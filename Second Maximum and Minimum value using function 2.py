list1=[]
list2=[]
n=int(input("Enter the length of list:"))
for i in range(n):
    e=int(input("Enter %d element:"%(i+1)))
    list1.append(e)
print("The list is:",list1)
for i in list1:
    if i not in list2:
        list2.append(i)
print("The list without repeated elements is:",list2)
for i in range(0,len(list2)):
    for j in range(i+1,len(list2)):
        if list2[i]>list2[j]:
            list2[i],list2[j]=list2[j],list2[i]
print("The new list is:",list2)            
def Second_Maximum_value(list2):
    first_maxval=list2[0]
    for i in list2:
        if i>first_maxval:
            first_maxval=i
    second_maxval=list2[0]
    for i in list2:
        if i>second_maxval and i!=first_maxval:
            second_maxval=i
    print("Second maximum value in the new list is:",second_maxval)
Second_Maximum_value(list2)

def Second_Minimum_value(list2):
    first_minval=list2[len(list2)-1]
    for i in list2:
        if i<first_minval:
            first_minval=i
    second_minval=list2[len(list2)-1]
    for i in list2:
        if i<second_minval and i!=first_minval:
            second_minval=i
    print("Second minimum value in the new list is:",second_minval)        
Second_Minimum_value(list2)
    
    





