def EvenOdd(n):

    if(n%2==0):
        return True
    elif(n%2!=0):
        return False
    else:
        return EvenOdd(n)

number=int(input("Enter number:"))
if(EvenOdd(number)):
    print(number,"is even")
else:
    print(number,"is odd")
    
