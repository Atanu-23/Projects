num1=float(input("Enter First number: "))
num2=float(input("Enter Second number: "))
i=1
while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        gcd=i
    i=i+1
print("The gcd of two number %f"%num1,"and %f"%num2,"is: ",gcd)
lcm=(num1*num2)/gcd
print("The lcm of two number %f"%num1,"and %f"%num2,"is: ",lcm)
