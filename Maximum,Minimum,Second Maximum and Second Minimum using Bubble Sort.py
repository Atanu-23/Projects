n=int(input("Enter the lngth of list:"))
l=[]
for i in range(n):
    a=int(input("Enter element"+str(i+1)+":"))
    l.append(a)
print("The list is:",l)
max=min=l[0]
print("\n")
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("The sorted list is:",l)                    
print("\n")
def Maximum(l,max):
    for i in range(n):
        if l[i]>max:
            max=l[i]
    print("The maximum number in a list is:",max)
Maximum(l,max)
print("\n")
def Minimum(l,min):
    for i in range(n):
        if l[i]<min:
            min=l[i]
    print("The minimum number in a list is:",min)
Minimum(l,min)    
second_max=second_min=0
print("\n")
def Second_max(l,second_max):
    first_max=l[0]
    for i in l:
        if i>first_max:
            first_max=i
            second_max=l[0]
        for i in l:
            if i>second_max and i!=first_max:
                second_max=i
    print("Second maximum value in the list is:",second_max)
Second_max(l,second_max)
print("\n")
def Second_min(l,second_min):
    first_min=l[len(l)-1]
    for i in l:
        if i<first_min:
            first_min=i
            second_min=l[len(l)-1]
        for i in l:
            if i<second_min and i!=first_min:
                second_min=i
    print("Second minimum value in the list is:",second_min)
Second_min(l,second_min)
