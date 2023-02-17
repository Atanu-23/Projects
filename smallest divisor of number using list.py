n=int(input("Enter the integer: "))
l=[]
for i in range(2,n):
    if n%i==0:
        l.append(i)
l.sort()
print("The smallest divisor of number is: ",l[0])
