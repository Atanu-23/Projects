String=input("Enter the string:")
lower_count=upper_count=0
for i in String:
    if (i>="A" and i<="Z"):
        upper_count+=1
    elif(i>="a" and i<="z"):
        lower_count+=1
print("\n")        
print("The number of upper character in the string is:",upper_count)
print("\n")
print("The number of lower character in the string is:",lower_count)
