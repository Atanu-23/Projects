print("This is a program to reverse a string")
print()
print("Put 1 for process 1")
print()
print("Put 2 for process 2")
print()
print("Put 3 for process 3")
print()
print("Put 4 for process 4")
print()
print("Put 5 for process 5")
print()
print("Put 6 for process 6")
print()
print("\n")
n=int(input("Enter your choice:"))
print()
if n==1:
    def Reverse1(String1):
        str=""
        for i in String1:
            str=i+str
        return str
    String1=input("Enter String:")
    print()
    print("Original string is: ",String1)
    print()
    print("Reverse of String is: ",Reverse1(String1))
    print("\n\n")
    print()
elif n==2:
    def Reverse2(String2):
        if len(String2)==0:
            return String2
        else:
            return Reverse2(String2[1:])+String2[0]
    String2=input("Enter String:")
    print()
    print("Original string is: ",String2)
    print()
    print("Reverse of String is: ",Reverse2(String2))
    print("\n\n")
    print()
elif n==3:
    def Reverse3(string):
        string=string[::-1]
        return string
    String3=input("Enter String:")
    print()
    print("Original String is: ",String3)
    print()
    print("Reverse of String is: ",Reverse3(String3))
    print("\n\n")
    print()
elif n==4:
    def Reverse4(string):
        string="".join(reversed(string))
        return string
    String4=input("Enter String:")
    print()
    print("Original String is:",String4)
    print()
    print("Reverse String is:",Reverse4(String4))
    print("\n\n")
    print()
elif n==5:
    def Reverse5(string):
        string=[string[i] for i in range (len(string)-1,-1,-1)]
        return "".join(string)
    String5=input("Enter String:")
    print()
    print("Original String is:",String5)
    print()
    print("Reverse String is:",Reverse5(String5))
    print("\n\n")
    print()
elif n==6:
    def Reverse6(string):
        string=list(string)
        string.reverse()
        return "".join(string)
    String6=input("Enter String:")
    print()
    print("Original String is:",String6)
    print()
    print("Reverse String is:",Reverse6(String6))
    print("\n\n")
    print()
else:
    print("Default input.Please give choice between 1 to 6!!")
