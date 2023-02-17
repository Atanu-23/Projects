n=int(input("ENETR THE NUMBER: "))
print("THE FACTORS OF %d ARE:"%n)
a=n
sum=0
for i in range(1,n):
    if(n%i==0):
        print(i)
        sum=sum+i
print("THE SUM OF FACTORS OF %d IS:"%a)
print(sum)        
if n==sum:
    print("THE NUMBER IS A PERFECT NUMBER")
else:
    print("THE NUMBER IS NOT A PERFECT NUMBER")
