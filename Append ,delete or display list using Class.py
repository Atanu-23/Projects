class Check():
    def __init__(self):
        self.l=[]

    def Add(self,a):
        return self.l.append(a)

    def Delete(self,b):
        return self.l.remove(b)

    def Display(self):
        return self.l

obj=Check()    


print("Choice 1 for Add")
print("Choice 2 for Delete")
print("Choice 3 for Display")
print("Choice 0 for Exit")
choice=1

while choice!=0:
    choice=int(input("Enter your choice:"))
    if choice==1:
        m=int(input("Enter number of elements:"))
        for i in range(1,m+1):
            e=int(input("Enter element"+str(i)+":"))
            obj.Add(e)
        print("List is:",obj.Display())
    elif choice==2:
        n=int(input("Enter number of elements:"))
        for i in range(1,n+1):
            e=int(input("Enter number"+str(i)+":"))
            obj.Delete(e)
        print("List is:",obj.Display())
    elif choice==3:
        print("List is:",obj.Display())
    elif choice>3:
        print("Invalid Choice!!")
    else:
        print("Exiting!!")
print()        
