m=int(input("Enter number of list:"))
print()
list1=[]
list2=[]
for i in range(1,m+1):
    n=int(input("Enter length of list"+str(i)+":"))
    for j in range(0,n):
        e=int(input("Enter element"+str(j+1)+":"))
        list1.append(e)
    list2.append(list1)
    list1=[]
a=int(input("Enter number of element:"))
for g in range(1,a+1):
    h=int(input("give element"+str(g)+":"))
    list2.append(h)    
print("The list of list and element is:",list2)
print()
print("This is a process for flattening a list")
print()
print("Press 1 for process 1")
print()
print("Press 2 for process 2")
print()
a=int(input("Enter your choice:"))
print()
if a==1:
    def Flatten(l):
        result=[]
        stack=[l]

        while stack:
            current=stack.pop(-1)

            if isinstance(current,list):
                stack.extend(current)
            else:
                result.append(current)

        result.reverse()
        return result
    print("The list after flattening is:",Flatten(list2))

elif a==2:
    from iteration_utilities import deepflatten
    answer=list(deepflatten(list2))
    print("The list after flattening is:",answer)

else:
    print("Default Input.Give choice 1 or 2!")
