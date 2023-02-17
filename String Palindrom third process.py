String=input("Enter ths String:")
def IsPalindrom(String):
    return String==String[::-1]
answer=IsPalindrom(String)
if(answer):
    print("String is Palindrom")
else:
    print("String is not Palindrom")
    
