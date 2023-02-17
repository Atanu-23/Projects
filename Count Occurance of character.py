String=input("Enter the String:")
char=input("Enter the word you want to count appearance:")
def CountWord(String,char):
    return String.count(char)
counter=CountWord(String,char)
if(counter>0):
    print("The number of occurance of character in the string is:",counter)
else:
    print("Character not found!!!")
    
