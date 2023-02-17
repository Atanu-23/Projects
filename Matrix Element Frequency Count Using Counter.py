from collections import Counter
import itertools
import operator as op
row_list=[]
list_of_list=[]

for i in range(3):
    for j in range(3):
        element=int(input("Give element"+str([j+1])+":"))
        row_list.append(element)
    list_of_list.append(row_list)
    row_list=[]

print("The original list is:",list_of_list)
print("\n")

choice=int(input("Give your choice:"))
print("\n")
if choice==1:
    res1=dict(sum(map(Counter,list_of_list),Counter()))
    print("The frequency dictionary is:",res1)

elif choice==2:
    res2=dict(Counter(itertools.chain(*list_of_list)))
    print("The frequency dictionary is:",res2)

elif choice==3:
    res3=dict()
    a=[]
    
    for i in list_of_list:
        a.extend(i)

    b=set(a)
    for i in b:
        res3[i]=a.count(i)

    print("The frequency dictionary is:",res3)

elif choice==4:
    res4=dict()
    a=[]
    
    for i in list_of_list:
        a.extend(i)

    b=set(a)
    for i in b:
        res4[i]=op.countOf(a,i)

    print("The frequency dictionary is:",res4)

else:
    print("Default Input!!")    
