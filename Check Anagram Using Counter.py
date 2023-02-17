from collections import Counter

def Anagram(String1,String2):
    return Counter(String1)==Counter(String2)

if __name__=="__main__":
    Input1=input("Give first String:")
    Input2=input("Give second String:")

    if Anagram(Input1,Input2)==True:
        print("Strings are Anagram")
    else:
        print("Strings are not Anagram")
