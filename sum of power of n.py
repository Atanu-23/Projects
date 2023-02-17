n=int(input("Enter the number n: "))
sum=0
for i in range(1,n+1):
    print(n**i,end='')
    if i==n:
        break
    print("+",end='')
for i in range(1,n+1):
    sum=sum+n**i
print("=",sum,end='')    
    
