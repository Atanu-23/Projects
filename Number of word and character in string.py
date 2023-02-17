import string
String=input("Enter the String:")
word_count=String.split()
print("The number of word in the string is:",len(word_count))
char_count=0
for word in word_count:
    char_count=char_count+len(word)
print("The number of character in the string is:",char_count)    

