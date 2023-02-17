fibonacciarray=[0,1]

def FibonacciSeries(n):
    if n<0:
        print("Default input")
    elif n<len(fibonacciarray):
        return fibonacciarray[n]
    else:
        fibonacciarray.append(FibonacciSeries(n-1)+FibonacciSeries(n-2))
        return fibonacciarray[n]

number=int(input("Enter number:"))
print("Fibonacci Series upto "+str(number)+"th term is:")

for i in range(number+1):
    print(FibonacciSeries(i),end=" ")
