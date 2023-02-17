def EvenOdd(n):
    if n==0:
        return True

    elif n==1:
        return False

    else:
        return EvenOdd(n-2)

num=int(input("Enter the number:"))

if(EvenOdd(num)):
    print(num,"is even")
else:
    print(num,"is odd")
    
        
