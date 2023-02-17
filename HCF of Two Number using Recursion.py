def HCF(a,b):

    if (a==0):
        return b

    elif (b==0):
        return a

    else:
        return HCF(b,a%b)

x=int(input("Give first number:"))
print()
y=int(input("Give second number:"))
print()
print("The gcd of "+str(x)+" and "+str(y)+" is:",HCF(x,y))
print()
def GCD(a,b):

    if(a==0):
        return b

    elif(b==0):
        return a

    elif(a==b):
        return a

    elif(a>b):
        return GCD(a-b,b)
    return GCD(a,b-a)
x=int(input("Give first number:"))
print()
y=int(input("Give second number:"))
print()
print("The gcd of "+str(x)+" and "+str(y)+" is:",GCD(x,y))
        
