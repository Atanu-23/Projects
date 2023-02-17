lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
r=int(input("Enter the number by which division is done: "))
print("The numbers are:")
for i in range(lower,upper+1):
    if i%r==0:
        print(i)
   
