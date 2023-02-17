num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
temp=0
if num1>num2:
    temp=num1-num2
else:
    temp=num2-num1
for i in range(1,temp+1):
    if(num1%i==0 and num2%i==0):
        gcd=i
print("The gcd of two numbers %f"%num1,"and %f"%num2,"is: ",gcd)        
lcm=(num1*num2)/gcd
print("The lcm of two numbers %f"%num1,"and %f"%num2,"is: ",lcm)
