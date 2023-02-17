n=int(input("Enter the range: "))
x=float(input("Enter the value: "))
sum=0
for i in range(2,n+1):
    sum=1+sum+(1/(n**i))
print("The sum of Series is 1",end='')
for i in range(2,n+1):
    if i==n:
        print("=",end='')
        break
    else:
        print("+",end='')
        print(1/n**i,end='')
print(sum)        
