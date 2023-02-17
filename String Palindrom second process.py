String=input("Enter the String:")
def CheckPalindrom(String):
    Reversedstring=String[::-1]
    status=1
    if(String!=Reversedstring):
        status=0
    return status
status=CheckPalindrom(String)
if(status):
    print("String is Palindrom")
else:
    print("String is not Palindrom")
