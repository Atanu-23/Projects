n=int(input("Enter the number: "))
print("The numbers from 1 to %d are:"%n)
def Print_num(n):
    if(n>0):
        Print_num(n-1)
        print(n," ",end='')
Print_num(n)        
    
    
