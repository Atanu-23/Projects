n=int(input("ENTER THE NUMBER: "))
a=n
sum=0
while n!=0:
    fact=1
    i=1
    d=n%10
    while i<=d:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
print("THE SUM OF FACTORIAL OF DIGIT OF THE NUMBER %d IS:"%a,sum)
if a==sum:
    print("THE NUMBER IS STRONG NUMBER")
else:
    print("THE NUMBER IS NOT STRONG NUMBER")
    
