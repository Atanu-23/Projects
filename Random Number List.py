import random
n=int(input("Enter the number of numbers want in the list:"))
l=[]
upper=int(input("Enter the upper range:"))
lower=int(input("Enter the lower range:"))
def Random_Integer(upper,lower,l):
    for i in range(n):
        rn=random.randint(lower,upper)
        l.append(rn)
    print("The list of ramdom number is:",l)
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print("The sorted list is:",l)            
Random_Integer(lower,upper,l)

            
