String=input("Enter the String:")
char=input("Enter the word you want to find number of occurance:")
count=0
for i in range(len(String)):
    if String[i]==char:
       count=count+1
if(count>0):
    print("Number of occurance of "+char+" in the String is:",count)
else:
    print("Character not found!!!")
