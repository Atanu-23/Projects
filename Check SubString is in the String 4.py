S1=input("Enter the String:")
S2=input("Enter the Substring you want to find:")
def CheckString(S1,S2):
    if S1.count(S2)>0:
        print("Yes the Substring is in the String!!!")
    else:
        print("No the Substring is not in the String")
CheckString(S1,S2)

        
