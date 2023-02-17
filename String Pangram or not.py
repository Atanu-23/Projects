import string
String=input("Enter the String:")
alphabet=set(string.ascii_lowercase)
def IsPangram(String):
    return set(String.lower())>=alphabet
if(IsPangram(String)==True):
    print("String is Pangram")
else:
    print("String is not Pangram")
    
    
