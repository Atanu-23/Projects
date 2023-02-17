class my_dictionary(dict):

    def __init__(self):
        self=dict()

    def add(self,key,value):
        self[key]=value

dict_obj=my_dictionary()

dict_obj.add(1,'Hello')
dict_obj.add(2,'World')

n=int(input("Enter the length of dictionary:"))
for i in range(n):
    dict_obj.key=input("Enter the key:")
    dict_obj.value=input("Enter the value:")
    dict_obj.add(dict_obj.key,dict_obj.value)

print(dict_obj)
    
