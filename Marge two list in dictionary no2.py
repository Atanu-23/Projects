keys=[]
values=[]
n=int(input("Enter total number of keys:"))
for i in range(n):
    c=input("Enter element"+str(i+1)+":")
    keys.append(c)
print("The list of keys are:",keys)
print("\n")

m=int(input("Enter total number of values:"))
for j in range(m):
    e=input("Enter element"+str(j+1)+":")
    values.append(e)
print("The list of values are:",values)
print("\n")

dictionary={key:value for key,value in zip(keys,values)}
print("The dictionary made from two lists are",dictionary)
