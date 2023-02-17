def NewString(String1):
    String2=''
    for i in range(len(String1)):
        if i%2==0:
            String2=String2+String1[i]
    return String2
String1=input("Enter the String:")
print("Original string was:",String1)
print("New string is:",NewString(String1))
