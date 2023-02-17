from collections import Counter

print("Prees 1 for counter using list")
print("Press 2 for counter using dictionary")
choice=int(input("Give your choice:"))

if choice==1:
    #With sequence of item using list
    l=[]
    n=int(input("Enter length of list:"))
    for i in range(n):
        element=input("Give element"+str(i+1)+":")
        l.append(element)
    print("The counter made from list is:",Counter(l))

elif choice==2:
    class Dictionary(dict):

        def __init__(self):
            self=dict()

        def add(self,key,value):
            self[key]=value

    dictionary=Dictionary()

    n=int(input("Enter length of dictionary:"))
    for i in range(n):
        dict_key=input("Give key"+str(i+1)+":")
        dict_value=input("Give value"+str(i+1)+":")
        dictionary.add(dict_key,dict_value)
    print("The Counter nade from dictionary is:",Counter(dictionary))

else:
    print("Default input!!")

print("Choose 1 for Update the Counter")
print("Choose 2 for delete from Counter")
print("Choose 3 for Addition of two Counter")
print("Choose 4 for Subtraction of two Counter")
print("Choose 5 for Union of two Counter")
print("Choose 6 for Intersection of two Counter")
choose_operation=int(input("Choose operation you want to perform:"))

coun1=coun2=Counter(l)
if choose_operation==1:
    m=int(input("Enter number of element you want to add:"))
    l2=[]
    for i in range(m):
        e=input("Give element"+str(i+1)+":")
        l2.append(e)
    coun1.update(l2)
    print("The new counter is:",coun1)

elif choose_operation==2:
    a=int(input("Give number of element you want to delete:"))
    l3=[]
    for i in range(a):
        e=input("Give element"+str(i+1)+":")
        del coun2[e]
    print("The new counter is:",coun2)

elif choose_operation==3:
    n1=int(input("Enter length of list:"))
    l1=[]
    for i in range(n1):
        element=input("Give element"+str(i+1)+":")
        l1.append(element)
        t1=Counter(l1)
    print("The counter made from list is:",t1)
    n2=int(input("Enter length of list:"))
    l2=[]
    for i in range(n2):
        element=input("Give element"+str(i+1)+":")
        l2.append(element)
        t2=Counter(l2)
    print("The counter made from list is:",t2)
    print("New counter made from addition of two counter is:",t1+t2)

elif choose_operation==4:
    n3=int(input("Enter length of list:"))
    l3=[]
    for i in range(n3):
        element=input("Give element"+str(i+1)+":")
        l3.append(element)
        t3=Counter(l3)
    print("The counter made from list is:",t3)
    n4=int(input("Enter length of list:"))
    l4=[]
    for i in range(n4):
        element=input("Give element"+str(i+1)+":")
        l4.append(element)
        t4=Counter(l4)
    print("The counter made from list is:",t4)
    print("New counter made from subtraction of two counter is:",t3-t4)
    print("New counter made from subtraction of two counter is:",t4-t3)

elif choose_operation==5:
    n5=int(input("Enter length of list:"))
    l5=[]
    for i in range(n5):
        element=input("Give element"+str(i+1)+":")
        l5.append(element)
        t5=Counter(l5)
    print("The counter made from list is:",t5)
    n6=int(input("Enter length of list:"))
    l6=[]
    for i in range(n6):
        element=input("Give element"+str(i+1)+":")
        l6.append(element)
        t6=Counter(l6)
    print("The counter made from list is:",t6)
    print("The new counter made by union of two counter is:",t5|t6)
    
elif choose_operation==6:
    n7=int(input("Enter length of list:"))
    l7=[]
    for i in range(n7):
        element=input("Give element"+str(i+1)+":")
        l7.append(element)
        t7=Counter(l7)
    print("The counter made from list is:",t7)
    n8=int(input("Enter length of list:"))
    l8=[]
    for i in range(n8):
        element=input("Give element"+str(i+1)+":")
        l8.append(element)
        t8=Counter(l8)
    print("The counter made from list is:",t8)
    print("The new counter made by union of two counter is:",t7&t8)

else:
    print("Default Operation")
