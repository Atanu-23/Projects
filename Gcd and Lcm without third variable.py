num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
a=num1
b=num2
if num1==0:
    print("The gcd of two number %f"%a,"and %f"%b,"is: ",num1)
while num1!=num2:
    if num1>num2:
        num1=num1-num2
    else:
        num1=num2-num1
gcd=num1
print("The gcd of two number %f"%a,"and %f"%b,"is: ",num1)
lcm=(a*b)/gcd
print("The lcm of two number %f"%a,"and %f"%b,"is: ",lcm)
