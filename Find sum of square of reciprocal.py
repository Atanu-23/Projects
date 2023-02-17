sum=0
n=int(input("Enter the range of series: "))
x=int(input("Enter value: "))
for i in range(2,n+1):
    sum=sum+1+1/(x**i)
print("The sum of series upto %d"%n,"terms is: ",sum)    


print("Using function:")
def Series_2(n):
    sum=0
    for i in range(2,n+1):
        sum=sum+1+1/(x**i)
    print("The sum of series upto %d"%n,"terms is: ",sum)
Series_2(n)    
