String=input("Enter the Word:")
dictionary={}
for i in String:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
print("The dictionary made from letters of word is:",dictionary)
