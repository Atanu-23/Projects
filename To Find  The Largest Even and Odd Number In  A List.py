n=int(input("ENTER NUMBER OF ELEMENTS OF THE LIST: "))
a=0
b=[]
evenlist=[]
oddlist=[]
evensum=0
oddsum=0
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
for i in b:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
evenlist.sort()
oddlist.sort()
count1=0
count2=0
for j in evenlist:
    count1=count1+1
    evensum=evensum+j
for k in oddlist:
    count2=count2+1
    oddsum=oddsum+k
print("tHE LARGEST EVEN NUMBER IN EVEN NUMBER LIST IS: ", evenlist[count1-1])
print("THE LARGEST ODD NUMBER IN ODD NUMBER LIST IS: ", oddlist[count2-1])
print("THE SECOND LARGEST NUMBER IN EVEN NUMBER LIST IS: ",evenlist[count1-2])
print("THE SECOND LARGEST NUMBER IN ODD NUMBER LIST IS: ",oddlist[count2-2])
print("THE SUM OF ELEMENTS IN THE EVEN NUMBER LIST IS: ",evensum)
print("THE SUM OF ELEMENTS IN THE ODD LIST IS: ",oddsum)
