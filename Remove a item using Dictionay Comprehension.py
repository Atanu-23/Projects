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
print("The dictionary before removing items is:",dictionary)

Item=input("Enter item you want to remove:")
def RemoveItem(dictionary,Item):
    new_dictionary={key:val for key,val in dictionary.items() if key!=Item}
    print("The dictionary after removing item is:",new_dictionary)
RemoveItem(dictionary,Item)   

anotheritem=input("Enter another item you want to remove:")
def removeitem(dictionary,anotheritem):
    New_dictionary={key:dictionary[key] for key in dictionary if key!=anotheritem}
    print("The new dictionary after removing item is:",New_dictionary)
removeitem(dictionary,anotheritem)

    
