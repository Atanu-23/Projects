import math
a=0
x=float(input("Enter the value in degree: "))
n=int(input("Enter number of terms: "))
pi=math.pi
a=x*(pi/180)
print("The value in radian is: ",a)
def Sine(x,n):
    fact=1
    sum=0
    for i in range(0,n):
        sign=(-1)**i
        sum=sum+sign*(a**(2*i+1))/math.factorial(2*i+1)
    print("The Sine value of %d degree"%x,"in %d numbers of interval"%n,"is: ",sum)    
Sine(x,n)    
def Cosine(x,n):
    fact=1
    sum=0
    for i in range(0,n):
        sign=(-1)**i
        sum=sum+sign*(a**(2*i))/math.factorial(2*i)
    print("The Cosine value of %d degree"%x,"in %d numbers of interval"%n,"is: ",sum)
Cosine(x,n)
