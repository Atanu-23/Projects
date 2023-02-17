import string
String=input("Enter the String:")
def IsPangram(String):
    Alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in Alphabet:
        if char not in String.lower():
            return False
    return True
if(IsPangram(String)==True):
    print("String is Pangram")
else:
    print("String is not Pangram")
    
