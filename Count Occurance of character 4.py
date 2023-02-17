import re
InputString=input("Enter the String:")
char=input("Enter the character which we want to find occurance in String:")
count=len(re.findall(char,InputString))
print("Number of occurance of "+char+" in the String is:",count)
