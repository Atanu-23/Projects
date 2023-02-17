lower=int(input("ENTER THE LOWER LIMIT: "))
upper=int(input("ENTER THE UPPER LIMIT: "))
print("THE NUMBER WHICH IS DIVISIBLE BY 7 AND MULTIPLYER OF 5 IS:")
for i in range(lower,upper+1):
    if i%5==0 and i%7==0:
        print(i)
    
