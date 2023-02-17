n=int(input("Enter the value: "))
print("The prime factors of number %d is"%n)
while n%2==0:
        d=2
        print(d)
        n=n//2
for i in range(3,n+1,2):
    while(n%i==0):
           a=i
           print(a)
           n=n//i
        
        
