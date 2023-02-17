l=[]
n=int(input("Enter length of array:"))
for i in range(n):
    e=int(input("Enter element"+str(i+1)+":"))
    l.append(e)
    
a=bytearray(l)
print("The bytearray is:",a)

position=int(input("Enter the position:"))
if position <=len(l):
    element=int(input("Give element:"))
    a[position]=element

else:
    print("Default Position!1")
print("Updated bytearray is:",a)    

new_element=int(input("Enter element:"))
a.append(new_element)
print("After adding element",a)
