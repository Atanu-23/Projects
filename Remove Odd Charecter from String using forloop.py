String1 = input("Enter the String:")
String2 = ''
for i in range(0,len(String1)):
    if(i % 2 == 0):
        String2 = String2 + String1[i]
print("Original String was:",String1)
print("Final String is:", String2)
