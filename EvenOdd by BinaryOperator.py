def EvenOdd(n):

    if(n & 1):
        return False
    else:
        return True
number=int(input("Enter number:"))

if(EvenOdd(number)):
    print(number,"is even")
else:
    print(number,"is odd")
