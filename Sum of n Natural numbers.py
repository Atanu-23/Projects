sum=0
n=int(input("Enter the number of natural number: "))
sum=n*(n+1)/2
print("The sum of first %d"%n,"Natural numbers is: ",sum)

print("Using Function")
def sum_of_numbers(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print("The sum of first %d"%n,"Natural number is: ",sum)
sum_of_numbers(n)    
