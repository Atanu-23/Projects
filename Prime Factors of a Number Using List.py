n=int(input("ENTER THE NUMBER: "))
factors=[]
print("THE PRIME FACTORS OF NUMBER %d IS"%n)
while n%2==0:
    factors.append(2)
    n//=2
divisor=3
while n!=1 and divisor<=n:
    if n%divisor==0:
        factors.append(divisor)
        n//=divisor
    else:
        divisor+=2
for i in range(len(factors)):
    print(factors[i],end=' ')
    
    
