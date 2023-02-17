def IsPrime(n,i=2):
    if(n<=2):
        return True if (n==2) else False

    if (n%i==0):
        return False

    if(i*i>n):
        return True
    return IsPrime(n,i+1)

number=int(input("Give a Number:"))

if(IsPrime(number)==True):
    print(str(number)+" is prime")
else:
    print(str(number)+" is not prime")
