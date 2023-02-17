from collections import Counter
list1=[]
n=int(input("Give length of list:"))
for i in range(n):
    element=input("Give element"+str(i+1)+":")
    list1.append(element)
counter_list=Counter(list1)
print("Counter is:",counter_list)
print("\n")

items=counter_list.items()
print(items)
print("Items are:")
for i in items:
    print(i)
print("\n")

keys=counter_list.keys()
print(keys)
print("Keys are:")
for j in keys:
    print(j)
print("\n")

values=counter_list.values()
print(values)
print("Values are")
for k in values:
    print(k)
print("\n")

