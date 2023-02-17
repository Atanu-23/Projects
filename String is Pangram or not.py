import string
String=input("Enter the String:")
Alphabet=set(string.ascii_lowercase)
def IsPangram(String):
    return not set(Alphabet)-set(String)
if(IsPangram(String)==True):
    print("String is Pangram")
else:
    print("String is not Pangram")
    
