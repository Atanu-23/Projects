sum=0
l=[]
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The factors of number %d is:"%a,end='')
for i in range(1,a):
    if(a%i==0):
        print(i,end=' ')
        l.append(i)
for j in l:
    sum=sum+j
print()    
print("The sum of factors of %d"%a,"is: ",sum)
if(b==sum):
    print("The two number %d"%a,"and %d"%b,"is amicable")
else:
    print("The two number %d"%a,"and %d"%b,"is not amicable")
          
          
    
