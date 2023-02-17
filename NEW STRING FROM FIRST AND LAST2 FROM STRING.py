InputString=input("Enter the String:")
count=0
for i in InputString:
    count=count+1
NewString=InputString[0:2]+InputString[count-2:count]
print("The new string is:",NewString)
