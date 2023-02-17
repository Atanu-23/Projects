String=input("Enter the string:")
count1=count2=0
for i in String:
    if i.islower():
        count1=count1+1
    elif i.isupper():
        count2=count2+1
print("Number of uppercase character in the String is:",count2)
print("Number of lowercase character in the String is:",count1)        
