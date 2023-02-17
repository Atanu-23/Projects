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
print("The Dictionary is:",dictionary)

def findproduct1(dictionary):
    pro1=1
    for i in dictionary:
        pro1=pro1*dictionary[i]
    return pro1
print("The product of item is:",findproduct1(dictionary))
        
def findproduct2(dictionary):
    pro2=1
    for i in dictionary.values():
        pro2=pro2*i
    return pro2
print("The product if item in dictionary is:",findproduct2(dictionary))
