String=input("Enter the string:")
def ChangeString(String):
    return String[-1:]+String[1:-1]+String[:1]
print("The changed string is:",end="")
print(ChangeString(String))
