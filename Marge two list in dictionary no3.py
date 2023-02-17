Keys=[]
Values=[]
n=int(input("Enter length of list of Keys:"))
for i in range(n):
    c=input("Enter element"+str(i+1)+":")
    Keys.append(c)
print("The list of keys is:",Keys)
print()

m=int(input("Enter length of list of Values:"))
for j in range(m):
    e=input("Enter element"+str(j+1)+":")
    Values.append(e)
print("The list of values is:",Values)
print()

List=zip(Keys,Values)

dictionary={}

for key,value in List:
    if key in dictionary:
        pass
    else:
        dictionary[key]=value
print("The dictionary of made of lists are:",dictionary)        
    
