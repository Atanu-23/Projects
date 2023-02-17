String=input("Enter the string:")
string=" "
s=String.split()
print(len(s))
for i in range(0,len(s)-1):
    string=string+s[i]+"-"
string1=string+s[-1]    
print("The String with Space is:",String)
print("The String with Hyphen is:",string1)
