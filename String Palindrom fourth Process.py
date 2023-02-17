String=input("Enter the String:")
def IsPalindrom(String):
    for i in range(0,int(len(String)/2)):
        if(String[i]!=String[len(String)-i-1]):
            return False
    return True
Answer=IsPalindrom(String)
if(Answer):
    print("String is Palindrom")
else:
    print("String is not Palindrom")
    

        
