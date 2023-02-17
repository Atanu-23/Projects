evensum=0
oddsum=0
n=int(input("ENTER THE NUMBER: "))
for i in range(1,n+1):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("The sum of even integers is %d"%evensum)
print("The sum of odd integers is %d"%oddsum)
