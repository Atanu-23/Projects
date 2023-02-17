n=int(input("Enter the number: "))
print("The divisor of number %d is: "%n)
for i in range(2,n+1):
    if(n%i==0):
        print(i)
        
