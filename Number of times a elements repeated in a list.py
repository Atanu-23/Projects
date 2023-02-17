l=[]
count=temp=index=0
n=int(input("Enter the length of list: "))
for i in range(n):
    a=int(input("Enter elements: "))
    l.append(a)
print(l)
for i in range(0,len(l)):
    temp=l.count(l[i])
    if temp>count:
        count=temp
        index=i
num=l[index]
print("The most frequent number in list is: ",num)
print("The number occured",count,"times in the list")

