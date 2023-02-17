String1=input("Enter the String:")
String2=''
i=0
while(i<len(String1)):
    if i%2==0:
        String2=String2+String1[i]
    i+=1
print("Original String is:",String1)
print("New String is:",String2)
