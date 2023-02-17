class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()        
String=input("Enter the String:")
for item in String:
    frequency=String.count(item)
    dictionary.add(item,frequency)
print("The dictionary made from word of string is:",dictionary)    
