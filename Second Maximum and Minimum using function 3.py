n=int(input("Enter the length of list:"))
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print("The list is:",l1)
for i in l1:
    if i not in l2:
        l2.append(i)
print("The list without any rapeated elements is:",l2)
    
def Secondmax(l2):
    s_max=0    
    max=l2[-1]
    for i in range(-1,-(len(l2)),-1):
        if l2[i]==max:
            pass
        else:
            s_max=l2[i]
            break
    print("The second maximum in the list is:",s_max)
Secondmax(l2)     

def Secondmin(l2):
    s_min=0
    min=l2[0]
    for i in range(0,len(l2),1):
        if l2[i]==min:
            pass
        else:
            s_min=l2[i]
            break
    print("The second minimum in the list is:",s_min)
Secondmin(l2)    
            
