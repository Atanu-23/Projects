class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()

n=int(input("Enter the length of dictionary:"))
for i in range(n):
    dictionary.key=int(input("Enter key"+str(i)+":"))
    dictionary.value=dictionary.key*dictionary.key
    dictionary.add(dictionary.key,dictionary.value)
print("New dictionay is:",dictionary)    
