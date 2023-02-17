InputString=input("Enter the String:")
char=input("Enter the character which we want to find the occurance:")
count=sum(map(lambda x:1 if char in x else 0,InputString))
print("Number of occurance of "+char+" in the string is:",count)
