from collections import Counter

def CommonWord(String1,String2):
    dict1=Counter(String1)
    dict2=Counter(String2)

    commondict=dict1 & dict2

    if len(commondict)==0:
        return -1

    commonchar=list(commondict.elements())

    commonword=sorted(commonchar)

    print("The common words between two strings are:",','.join(commonword))

if __name__=="__main__":
    String1=input("Enter first word:")
    String2=input("Enter second word:")
    CommonWord(String1,String2)
    
