class My_Dictionary(dict):

    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dict1=My_Dictionary()
n=int(input("Enter the length of first dictionary:"))
for i in range(n):
    dict1.key=input("Enter the key"+str(i+1)+":")
    dict1.value=input("Enter the value"+str(i+1)+":")
    dict1.add(dict1.key,dict1.value)
print("First dictionary is:",dict1)

dict2=My_Dictionary()
m=int(input("Enter the length of second dictionary:"))
for j in range(m):
    dict2.key=input("Enter the key"+str(j+1)+":")
    dict2.value=input("Enter the value"+str(j+1)+":")
    dict2.add(dict2.key,dict2.value)
print("Second dictionary is:",dict2)

dict3={**dict1,**dict2}
print("New Dictionary is:",dict3)


dict4=dict(dict1,**dict2)
print("New Dictionay by unpacking is:",dict4)
