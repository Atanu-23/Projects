n=int(input("Enter the number of element: "))
x=float(input("Enter the value: "))
list=[]
sum=0
for i in range(n):
    element=int(input("Enter the elements: "))
    list.append(element)    
for i in range(n):
    for i in list:
        sum=sum+list[i]*x**i
print(sum)        
for i in range(n):
    for i in list:
        print("The value of polynomial %d*x**%d"%list[i] %i,"at %f"%x,"is: ",sum)
