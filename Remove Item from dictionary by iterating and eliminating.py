class Mydictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=Mydictionary()

n=int(input("Enter the length of dictionary:"))
for i in range(n):
    dictionary.key=input("Enter key"+str(i+1)+":")
    dictionary.value=int(input("Enter value"+str(i+1)+":"))
    dictionary.add(dictionary.key,dictionary.value)
print("The dictionary before removing item is:",dictionary)

def RemoveaItem(dictionary):
    item=input("Enter item you want to remove:")
    new_dictionary={}
    for key,value in dictionary.items():
        if key!=item:
            new_dictionary[key]=value
    print("The dictionary after removing item is:",new_dictionary)
RemoveaItem(dictionary)    
