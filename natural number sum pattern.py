n=int(input("Enter the number: "))
sum=0
print("The natural number summation pattern is:")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
        if(j<i):
            print("+",end=' ')
    print('=',end=' ')
    sum=sum+i
    print(sum)
