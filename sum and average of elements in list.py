l=[]
sum=0
n=int(input("Enter the length of list: "))
for i in range(0,n):
    a=int(input("Enter elements: "))
    l.append(a)
print(l)
for i in range (0,len(l)):
    sum=sum+l[i]
print("The sum of elements in a list is: ",sum)
avg=sum/len(l)
print("The average of elements in a list is: ",avg)



