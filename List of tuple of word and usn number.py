n=int(input("Enter length of list of tuples:"))
t=()
tuplelist=[]
for i in range(n):
    e=input("Enter element"+str(i+1)+":")
    a=int(input("Enter number"+str(i+1)+":"))
    t=(e,a)
    tuplelist.append(t)
    t=()
print("The list of tuple is:",tuplelist)
lower=int(input("Enter lower roll number:"))
upper=int(input("Enter upper roll number:"))
newtuplelist=[]
for item in range(n):
    if tuplelist[item][1]>lower and tuplelist[item][1]<upper:
        newtuplelist.append(tuplelist[item])
print("The new list of tuple is:",newtuplelist)        
    
    


