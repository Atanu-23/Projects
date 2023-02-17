String=input("Enter the String:")
char=0
word=1
for i in String:
    char=char+1
    if i==" ":
        word=word+1
print("The number of words in the string is:",word)
print("The number of character in the string is:",char)
