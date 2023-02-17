String=input("Enter the string:")
print("{",end="")
for item in String:
    frequency=String.count(item)
    if String.index(item)==len(String)-1:
        print(str(item)+":"+str(frequency),end="")
    else:
        print(str(item)+":"+str(frequency)+",",end="")    
print("}")        

