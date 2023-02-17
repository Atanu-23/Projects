String1=input("Enter first string:")
String2=input("Enter second string:")
def IsAnagram(String1,String2):
    list1=list(String1)
    list2=list(String2)
    print(list1)
    print(list2)
    if(list1.sort()==list2.sort()):
        print("The two string is Anagram")
    else:
        print("The two string is not Anagram")
IsAnagram(String1,String2)

    
    
