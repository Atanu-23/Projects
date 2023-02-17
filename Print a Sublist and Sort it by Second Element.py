n=int(input("Enter the length of list:"))
list=[]
list1=[]
for i in range(n):
    e=int(input("Enter element"+str(i+1)+":"))
    list.append(e)
print("The list is:",list)
print("\n")
n1=int(input("Enter lower limit of sublist:"))
n2=int(input("Enter upper limit of sublist:"))
print("\n")
for i in range(n):
    for j in range(i+1,n):
        if list[i]==n1 and list[j]==n2:
          list1=list[i:j+1]
print("The sublist of list is given by",list1)
print("\n")    
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print("The sorted sublist is:",list1)            

