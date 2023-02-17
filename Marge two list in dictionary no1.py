list1=[]
list2=[]
n=int(input("Enter length of list1:"))
for i in range(n):
    c=input("Enter element"+str(i+1)+":")
    list1.append(c)
print("List of keys are:",list1)
print()

m=int(input("Enter length of list2:"))
for j in range(m):
    e=input("Enter element"+str(j+1)+":")
    list2.append(e)
print("List of values are:",list2)
print()

dictionary=dict(zip(list1,list2))
print("the dictionary made from two list is:",dictionary)

