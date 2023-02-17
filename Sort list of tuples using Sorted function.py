l=[]
list=[]
list1=[]
m=int(input("Enter the number of tuples:"))
for i in range(1,m+1):
    n=int(input("Enter length of list"+str(i)+":"))
    for j in range(n):
        e=int(input("Enter element"+str(j+1)+":"))
        list.append(e)
    t=tuple(list)
    list1.append(t)
    list=[]
    t=()
print("The original list of tuple is:",list1)
def last(m):
    return m[-1]
def Sort_list1_tuple(m):
    return sorted(list1,key=lambda x:x[-1])
print("The list of tuples in sorted order is:",end="")
print(Sort_list1_tuple(m))


        
