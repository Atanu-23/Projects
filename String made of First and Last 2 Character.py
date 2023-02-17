InputString=input("Enter the String:")
l=len(InputString)
NewString=""
for i in range(l):
    if i in (0,1,l-1,l-2):
        NewString=NewString+InputString[i]
print("Actual String is:"+InputString)
print("New String is:"+NewString)
