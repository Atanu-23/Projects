n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))

a=n1
b=n2
while(n2!=0):
    temp=n2
    n2=n1%n2
    n1=temp
    gcd=n1
print("The Gcd of two number %f"%a,"and %f"%b,"is: ",gcd)
lcm=(a*b)/gcd
print("The Lcm of two number %f"%a,"and %f"%b,"is: ",lcm)
