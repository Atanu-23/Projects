def IsPalindrom(st,s,e):

    if s==e:
        return True

    if st[s]!=st[e]:
        return False

    if s<e+1:
        return IsPalindrom(st,s+1,e-1)
    return True

def PalindromString(st):

    n=len(st)

    if n==0:
        return True
    return IsPalindrom(st,0,n-1)

String=input("Give the string:")
print()

if(PalindromString(String)):
    print("String is Palindrom")
else:
    print("String is not Palindrom")
    
