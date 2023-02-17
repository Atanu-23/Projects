lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper  limit: "))
print("The even numbers are:")
for i in range(lower,upper+1):
    if i%2==0:
        print(i)
print("The odd numbers are:")
for i in range(lower,upper+1):
    if i%2!=0:
        print(i)
        
