from array import *;
arr=array('i',[])
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The factors of %d is: "%a,end='')
for i in range(1,a):
    if a%i==0:
        print(i,end=' ')
        arr.append(i)
print()
print("The sum of factors of %d"%a,"is: ",sum(arr))
if sum(arr)==b:
    print("The two number %d"%a,"and %d"%b,"are amicable")
else:
    print("The two number %d"%a,"and %d"%b,"are not amicable")
