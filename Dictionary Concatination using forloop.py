class MyDictionary(dict):
    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value
        
dict1=MyDictionary()
n=int(input("Enter length of first dictionary:"))
for i in range(n):
    dict1.key=int(input("Enter the key"+str(i)+":"))
    dict1.value=input("Enter the value"+str(i)+":")
    dict1.add(dict1.key,dict1.value)
print("First dictionary is:",dict1)

dict2=MyDictionary()
m=int(input("Enter length of second dictionary:"))
for j in range(m):
    dict2.key=int(input("Enter the key"+str(j)+":"))
    dict2.value=input("Enter the value"+str(j)+":")
    dict2.add(dict2.key,dict2.value)
print("Second dictionary is:",dict2)

def MargeDictionary(dict1,dict2):
    dict3={**dict1,**dict2}
    for key,value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key]=[dict1[key],value]
    return dict3
dict3=MargeDictionary(dict1,dict2)
print("New Dictionary is:",dict3)

            
