import string
import itertools
String=input("Enter the String:")
Alphabet=set(string.ascii_lowercase)
def IsPangram(String):
    return sum(1 for i in set(String)if 96<ord(i)<=122)==26
if(IsPangram(String)==True):
    print("String is Pangram")
else:
    print("String is not Pangram")
    
    
