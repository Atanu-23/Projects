n=int(input("Enter the number n: "))
d=0
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("The reverse of number is: ",rev)    
