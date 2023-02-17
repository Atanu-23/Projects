print("Presss 1 for Tuple")
print("Pree 2 for List")
print("Press 3 for Dictionary")
p=int(input("Enter your choice:"))

if p==1:
    n=int(input("Enter the length:"))
    t=()
    for i in range(n):
        e=int(input("Enter element:"))
        t=t+(e,)
    print("Tuple is:",t)
    ftupleset=frozenset(t)
    print("Frozenset obtained from tuple is:",ftupleset)

elif p==2:
    n=int(input("Enter the length:"))
    l=[]
    for j in range(n):
        h=int(input("Enter element:"))
        l.append(h)
    print("List is:",l)
    flistset=frozenset(l)
    print("Frozenset obtained from list is:",flistset)

elif p==3:
    n=int(input("Enter the length:"))
    class Mydictionary(dict):

        def __init__(self):
            self=dict()

        def add(self,key,value):
            self[key]=value

    dictionary=Mydictionary()
    for k in range(n):
        dict_key=input("Enter key"+str(k)+":")
        dict_value=input("Enter value"+str(k)+":")
        dictionary.add(dict_key,dict_value)
    print("Dictionary is:",dictionary)
    fdictset=frozenset(dictionary)
    print("Frozenset made from keys of dictionary is:",fdictset)
    

else:
    print("Default input!!")

