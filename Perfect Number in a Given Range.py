lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
print("The perfect numbers are:")
for i in range(lower,upper+1):
    result=0
    for j in range(1,i):
        if i%j==0:
            result=result+j
    if i==result:
        print(i)
        
