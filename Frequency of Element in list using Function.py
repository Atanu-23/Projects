l=[]
c={}
temp=index=num=0
n=int(input("Enter range: "))
for i in range(0,n):
    a=int(input("Enter the element: "))
    l.append(a)
print(l)
def frequency_element(c,tempc,index,num):
    count=0
    for i in l:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    print("Frequency of each elements are:")        
    for key,value in c.items():
        print(key,"=",value)
    for i in range(0,len(l)):
        temp=l.count(l[i])
        if temp>count:
            count=temp
            index=i
    num=l[index]
    print("The element which has occured maximum times is: ",num)
    print("{} has occured {} times".format(num,count))
frequency_element(c,temp,index,num)    
