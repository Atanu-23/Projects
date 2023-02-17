n=int(input("Enter a integer: "))
for i in range(2,n):
    if n%i==0:
        print("The smallest divisor of integer is: ",i)
        break
    
