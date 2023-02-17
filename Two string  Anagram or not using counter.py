from collections import Counter 
string1=input("Enter the first string:")
string2=input("Enter the second string:")
def IsAnagram(string1,string2):
    c1=Counter(string1)
    c2=Counter(string2)
    if(c1==c2):
        print("The given two string is Anagram")
    else:
        print("The given two string is not Anagram")
IsAnagram(string1,string2)
