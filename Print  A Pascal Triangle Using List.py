n=int(input("ENTER NUMBER OF ROWS: "))
list=[]
for i in range(n):
    t_list=[]
    for j in range(i+1):
        if j==0 or j==i:
            t_list.append(1)
        else:
            t_list.append(list[i-1][j-1]+list[i-1][j])
    list.append(t_list)
print()


print("THE FIRST PASCAL TRIANGLE IS:")    

for i in range(n):
    for j in range(i+1):
        print(format(list[i][j],"<4"),end=" ")
    print()

print()

print("THE SECOND PASCAL TRIANGLE IS:")
    
for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2"),end="")
    for j in range(i+1):
        print(format(list[i][j],"<4"),end="")
    print()    
