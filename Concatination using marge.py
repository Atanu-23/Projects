class mydictionary(dict):
    def __init__(self):
        self=dict()
    def add(self,key,value):
        self[key]=value
        
dict1=mydictionary()
n=int(input("Enter length of first dictionary:"))
for i in range(n):
    dict1.key=input("Enter the key"+str(i+1)+":")
    dict1.value=input("Enter the value"+str(i+1)+":")
    dict1.add(dict1.key,dict1.value)
print("First dictionary is:",dict1)

dict2=mydictionary()
m=int(input("Enter length of second dictionary:"))
for j in range(m):
    dict2.key=input("Enter the key"+str(j+1)+":")
    dict2.value=input("Enter the value"+str(j+1)+":")
    dict2.add(dict2.key,dict2.value)
print("Second dictionary is:",dict2)
    
def Marge(dict1,dict2):
    result=dict1|dict2
    return result
dict3=Marge(dict1,dict2)
print("New marged dictionary is:",dict3)
