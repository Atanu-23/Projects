def lcm(a,b):
    lcm.multiple=lcm.multiple+b

    if((lcm.multiple%a==0)and(lcm.multiple%b==0)):
        return lcm.multiple

    else:
        lcm(a,b)

    return lcm.multiple
lcm.multiple=0

n1=int(input("Give first number:"))
print()
n2=int(input("Give second number:"))
print()

if(n1>n2):
    print("Lcm of "+str(n1)+" and "+str(n2)+" is: ",lcm(n2,n1))
else:
    print("Lcm of "+str(n1)+" and "+str(n2)+" is: ",lcm(n1,n2))
print()

def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif(b>a):
        return gcd(b%a,a)
    else:
        return gcd(a%b,a)

def lcm2(a,b):
    return (a/gcd(a,b))*b

n1=int(input("Give first number:"))
print()
n2=int(input("Give second number:"))
print()

print("Lcm of "+str(n1)+" and "+str(n2)+" is: ",lcm2(n1,n2))


            
    
    
