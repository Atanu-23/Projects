n=int(input("ENTER THE NUMBER: "))
count=d=0
b=a=n
sum=0
while n!=0:
    n=n//10
    count=count+1
while a!=0:
    d=a%10
    sum=sum+d**count
    a=a//10
if sum==b:
    print("THE NUMBER IS ARMSTRONG")
else:
    print("THE NUMBER IS NOT ARMSTRONG")
