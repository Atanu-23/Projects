String=input("Enter ths String:")
def CheckPalindrom(String):
    length=len(String)
    first=0
    last=length-1
    status=1
    while(first<last):
        if(String[first]==String[last]):
            first=first+1
            last=last-1
        else:
            status=0
            break
    return int(status)
status=CheckPalindrom(String)
if(status):
    print("String is Palindrom")
else:
    print("String is Not Palindrom")
