String1=input("Enter the first word:")
String2=input("Enter the second word:")

result=set(String1)-set(String2)
print("The words which are present in first word but not in second word is:",result)

commonword=(set(String1)^set(String2))
print("The words which are in words but not in both words are:",commonword)

commonletter=(set(String1)|set(String2))
print("The words which are present in both words are:",commonletter)

