class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()
n=int(input("Enter the length of Dictionary:"))
for i in range(n):
    dictionary.key=int(input("Enter key"+str(i)+":"))
    dictionary.value=input("Enter value"+str(i)+":")
    dictionary.add(dictionary.key,dictionary.value)
print("The Dictionary is:",dictionary)

key=int(input("Enter the key you want to find:"))
def CheckKey(dictionary,key):
    if key in dictionary.keys():
        print("Key is Present,",end=" ")
        print("Value:",dictionary[key])
    else:
        print("Key is not present")
CheckKey(dictionary,key)

anotherkey=int(input("Enter the another key you want to find:"))
def CheckKey2(dictionary,anotherkey):
    if anotherkey in dictionary:
        print("The Key is Present,",end=" ")
        print("Value:",dictionary[anotherkey])
    else:
        print("That Key is not present")
CheckKey2(dictionary,anotherkey)
