sum=0
n=int(input("Enter the range: "))
for i in range(1,n+1):
    sum=sum+(1/i)
print("The sum upto %d"%n,"terms is: ",sum)


print("Using Function:")

def Series_1(n):
    sum=0
    for i in range(n):
        sum=sum+1/(i+1)
    print("The sum upto %d"%n,"terms is: ",sum)
Series_1(n)    
