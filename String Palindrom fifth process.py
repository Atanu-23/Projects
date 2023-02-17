String=input("Enter the String:")
def IsPalindrom(String):
    Reverse="".join(reversed(String))
    if(Reverse==String):
        return True
    return False
Answer=IsPalindrom(String)
if(Answer):
    print("String is Palindrom")
else:
    print("String is not Palindrom")
    
