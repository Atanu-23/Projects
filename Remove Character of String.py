String=input("Enter a string:")
n=int(input("Enter the position of character you want to remove:"))
def RemoveCharacter(String,n):
    firstpart=String[:n]
    lastpart=String[n+1:]
    return firstpart+lastpart
RemoveCharacter(String,n)
print("The modified string is:",end="")
print(RemoveCharacter(String,n))
