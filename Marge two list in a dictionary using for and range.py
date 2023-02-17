Keys=[]
Values=[]
n=int(input("Enter length of list of keys:"))
for i in range(n):
    c=input("Enter element"+str(i+1)+":")
    Keys.append(c)
print("The list of keys is:",Keys)
print()

m=int(input("Enter length of list of values:"))
for j in range(m):
    e=input("Enter element"+str(j+1)+":")
    Values.append(e)
print("The list of values is:",Values)    
print()

dictionary={Keys[i]:Values[i] for i in range(len(Keys))}
print("The dictionary made from two list is:",dictionary)

