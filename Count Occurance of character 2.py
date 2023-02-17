from collections import Counter
InputString=input("Enter the String:")
char=input("Enter the character which we want to find the occurance:")
count=Counter(InputString)
print("The number of occurance of "+char+" in the string is:"+str(count[char]))
