class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def Add(self):
        return self.a+self.b

    def Subtract(self):
        if (self.a>self.b):
            return self.a-self.b
        else:
            return self.b-self.a

    def Multiply(self):
        return self.a*self.b

    def Divide(self):
        if (self.a>self.b):
            return self.a/self.b
        else:
            return self.b/self.a

first_number=float(input("Give first number:"))
second_number=float(input("Give second number:"))
print()

obj=Calculator(first_number,second_number)

choice=1
print("Choose 1 for Addition")
print("Choose 2 for Subtraction")
print("Choose 3 for Multiplication")
print("Choose 4 for Division")

while(choice!=0):
    choice=int(input("Enter your choice:"))

    if choice==1:
        print("Addition of two number is:",obj.Add())
        print()

    elif choice==2:
        print("Subtraction of two number is:",obj.Subtract())
        print()

    elif choice==3:
        print("Multiplication of two number is:",obj.Multiply())
        print()

    elif choice==4:
        print("Division of two number is:",obj.Divide())
        print()

    elif choice>4:
        print("Default input!!!")

    else:
        print("Exiting!!")  
    
            
