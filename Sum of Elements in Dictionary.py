class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dictionary=MyDictionary()
n=int(input("Enter length of Dictionary:"))
for i in range(n):
    dictionary.key=input("Enter key"+str(i)+":")
    dictionary.value=int(input("Enter value"+str(i)+":"))
    dictionary.add(dictionary.key,dictionary.value)
print("The dictionary is:",dictionary)

def SumofElements(dictionary):
    sum=0
    for i in dictionary:
        sum=sum+dictionary[i]
    return sum    
print("Sum of elements in dictionary is:",SumofElements(dictionary))
    
def SumofItem(dictionary):
    sum=0
    for i in dictionary.values():
        sum=sum+i
    return sum
print("The sum of all elements in dictionary is:",SumofItem(dictionary))
