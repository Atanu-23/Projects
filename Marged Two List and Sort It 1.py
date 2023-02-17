n1=int(input('Enter length of first list:'))
list1=[]
for i in range(n1):
    e=int(input('Enter element %d:'%(i+1)))
    list1.append(e)
print('The first list is:',list1)

n2=int(input('Enter length of second list:'))
list2=[]
for i in range(n2):
    c=int(input('Enter element %d:'%(i+1)))
    list2.append(c)
print('The second list is:',list2)
l=list1+list2
print('The marged list is:',l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print('The sorted marged list is:',l)

