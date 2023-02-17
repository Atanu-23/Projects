n=int(input("Enter a number:"))
def Fibonacci(n):
    a,b=0,1
    count=0

    if n<0:
        print("Default Input")

    elif n==0:
        print(0)

    elif n==1 or n==2:
        print(1) 

    else:
        print("Fibonacci Series upto "+str(n)+"th term is:")
        while count<n:
            print(a,end=" ")
            c=a+b
            a=b
            b=c
            count+=1
Fibonacci(n)        

print("\n")

def Fibonacci2(n):
    if n<=1:
        return n
    else:
        return (Fibonacci2(n-1)+Fibonacci2(n-2))

num=int(input("Give number:"))    
if num<=0:
    print("Give a positive number!!")
else:
    print("Fibonacci Series upto "+str(num)+"th term is:")
    for i in range(num):
        print(Fibonacci2(i),end=" ")
        
