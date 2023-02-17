String=input("Enter the string:")
lower_count=upper_count=0
for i in range(len(String)):
    if(ord(String[i])>=65 and ord(String[i])<=90):
        lower_count+=1
    elif(ord(String[i])>=97 and ord(String[i])<=122):
        upper_count+=1
print("The number of upper character in the string is:",upper_count)
print("The number of lower character in the string is:",lower_count)
