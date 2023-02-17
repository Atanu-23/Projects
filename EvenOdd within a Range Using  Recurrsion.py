def EvenOdd(a,b):
    
    if(a>b):
        return
    print(a,end=" ")
    return EvenOdd(a+2,b)

number1=int(input("Enter lower range:"))
number2=int(input("enter upper range:"))
temp=number1

print("even number in the range is:",end=" ")
if(number1%2==0):
    number1=number1
else:
   number1+=1
EvenOdd(number1,number2)

print()
number1=temp

print("Odd numbers in the range is:",end=" ")    
if(number1%2!=0):
    number1=number1
else:
   number1+=1
EvenOdd(number1,number2)    
