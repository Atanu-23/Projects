list=[]
Cum_list=[]
Cum2_list=[]
n=int(input("Enter the length of list:"))
for i in range(n):
    e=int(input("Enter element"+str(i+1)+":"))
    list.append(e)
print("The list of number is:",list)
print("\n")
def Less_Cumulative(list):
    sum=list[0]
    for j in range(1,n):
        sum=sum+list[j]
        Cum_list.append(sum)
    print("The less cumulative list of number is:",Cum_list)
    print("\n")
    for i in range(len(Cum_list)):
        for j in range(i+1,len(Cum_list)):
            if Cum_list[i]>Cum_list[j]:
                Cum_list[i],Cum_list[j]=Cum_list[j],Cum_list[i]
    print("The arranged less cumulative list of number is:",Cum_list)            
Less_Cumulative(list)
print("\n")
def Actual_Cumulative(list):
    sum=0
    for item in list:
        sum=sum+item
        Cum2_list.append(sum)
    print("The actual cumulative list of number is:",Cum2_list)
    print("\n")
    for i in range(len(Cum2_list)):
        for j in range(i+1,len(Cum2_list)):
            if Cum2_list[i]>Cum2_list[j]:
                Cum2_list[i],Cum2_list[j]=Cum2_list[j],Cum2_list[i]
    print("The arranged actual cumulative list of number is:",Cum2_list)            
Actual_Cumulative(list)    
