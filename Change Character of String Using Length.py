String=input("Enter a string:")
n=int(input("Enter the position of character you want to remove:"))
Str1=""
for i in range(len(String)):
    if i!=n:
        Str1=Str1+String[i]
print("The modified string is:",Str1)
