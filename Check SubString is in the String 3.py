String=input("Enter the String:")
SubString=input("enter the Substring you want to find in String:")
def CheckString(String,SubString):
    if(String.find(SubString)==-1):
        print("No the Substring is not in the String")
    else:
        print("Yes the Substring is in the String!!!")
CheckString(String,SubString)

        
