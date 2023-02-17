class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()
n=int(input("Enter length of Dictionary:"))
for i in range(n):
    dictionary.key=int(input("Enter key"+str(i)+":"))
    dictionary.value=input("Enter value"+str(i)+":")
    dictionary.add(dictionary.key,dictionary.value)
print("The dictionary is:",dictionary)

key=int(input("Enter the key you want to find:"))

if dictionary.get(key)==None:
    print("Key is not present")
else:
    print("Key is present,value=",dictionary[key])
    
anotherkey=int(input("Enter the other key you want to find:"))
try:
    dictionary[anotherkey]
    print("The key is present, value is:",dictionary[anotherkey])
except KeyError as error:
    print("The key is not present in dictionary")
    
