fact=1
sum=0
n=int(input("Enter the range: "))
for i in range(1,n+1):
    fact=fact*i
    sum=sum+1+1/fact
print("The sum of value of Euler function e=","upto %d range"%n,end='')
for i in range(1,n+1):
    if i==n:
        print("1/(%d)!"%n,end='')
        print("=")
        break
    else:
        print("1+",end='')
        print("1/(%d)!"%i,end='')
print(sum)        
