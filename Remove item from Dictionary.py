class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()

n=int(input("Enter the length of dictionary:"))
for i in range(n):
    dictionary.key=input("Enter key"+str(i)+":")
    dictionary.value=int(input("Enter value"+str(i)+":"))
    dictionary.add(dictionary.key,dictionary.value)
print("The dictionary is:",dictionary)

Item=input("Enter key you want to remove:")
del dictionary[Item]
print("The new dictionary is:",dictionary)



