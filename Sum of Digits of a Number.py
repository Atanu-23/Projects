def SumofDigit(n):

    if n==0:
        return 0
    else:
        return (n%10 + SumofDigit(int(n//10)))

number=int(input("Give the Number:"))
print()
print("The sum of digits of "+str(number)+" is:",SumofDigit(number))
