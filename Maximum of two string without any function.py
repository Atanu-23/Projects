string1=input("Enter first string:")
string2=input("Enter second string:")
print("The first string is:",string1)
print("The second string is:",string2)
length1=length2=length=0
for i in string1:
    length1=length1+1
for j in string2:
    length2=length2+1
if(length1>length2):
    print("The larger string is:",string1)
    print("Length of larger string is:",length1)
elif(length1==length2):
    length=length2
    print("The two string are equal")
    print("Length of each string is:",length)
else:
    print("The larger string is:",string2)
    print("Length of larger string is:",length2)
    
