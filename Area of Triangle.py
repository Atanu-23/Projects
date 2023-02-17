from math import *;
class Triangle:
    def Area(self):
        area=0
        s=0
        side1=int(input("Enter the first side: "))
        side2=int(input("Enter the second side: "))
        side3=int(input("Enter the third side: "))
        if (side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
            print("The triangle is possible")
            if(side1==side2==side3):
                print("The triangle is an equilateral triangle")
                area=(sqrt(3)/4)*side1**2
                print("The area of equilateral triagle is: ",area)
            elif(side1==side2 or side2==side3 or side3==side1):
                print("The triangle is an isoscales triangle")
                if(side1==side2):
                    area=(side3/2)*sqrt(side1**2-side3**2/4)
                    print("The area of isoscales triangle is: ",area)
                elif(side2==side3):
                    area=(side1/2)*sqrt(side2**2-side1**2/4)
                    print("The area of isoscales triangle is: ",area)
                else:
                    area=(side2/2)*sqrt(side3**2-side2**2/4)
                    print("The area of isoscales  triangle is: ",area)
            else:
                print("The triangle is a scalene triangle")
                s=(side1+side2+side3)/2
                area=sqrt(s*(s-side1)*(s-side2)*(s-side3))
                print("The area of scalene triangle is: ",area)
        else:
            print("The triangle is not possible")

Triangle.Area()         
