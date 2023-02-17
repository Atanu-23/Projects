import math
def calculate_area(name):
    name=name.lower()

    if name=="triangle":
        class Triangle():
            def __init__(self,side1,side2,side3):
                self.side1=side1
                self.side2=side2
                self.side3=side3

            def Triangle_Area(self):
                if(self.side1==self.side2==self.side3):
                    return (math.sqrt(3)/4*self.side1**2)

                elif (self.side1==self.side2 or self.side2==self.side3 or self.side3==self.side1):
                    if(self.side1==self.side2):
                        return (0.5*self.side3*math.sqrt((self.side1**2)-(self.side3**2)/4))
                    elif (self.side2==self.side3):
                        return (0.5*self.side1*math.sqrt((self.side2**2)-(self.side1**2)/4))
                    else:
                        return (0.5*self.side2*math.sqrt((self.side3**2)-(self.side2**2)/4))

                else:
                    self.S=(self.side1+self.side2+self.side3)/2
                    return (math.sqrt(self.S*(self.S-self.side1)*(self.S-self.side2)*(self.S-self.side3)))

        first_side=float(input("Give length of first side:"))
        second_side=float(input("Give length of second side:"))
        third_side=float(input("Give length of third side:"))

        obj=Triangle(first_side,second_side,third_side)
        print("Area of Triangle is:",obj.Triangle_Area())

    elif name=="parallelogram":
        class Parallelogram():
            def __init__(self,base,height):
                self.base=base
                self.height=height

            def Parallelogram_Area(self):
                return self.base*self.height

        a=float(input("Give length of base:"))
        b=float(input("Give length of height:"))

        obj=Parallelogram(a,b)
        print("Area of Parallelogram is:",obj.Parallelogram_Area())

    elif name=="trapezium":
        class Trapezium():
            def __init__(self,side1,side2,height):
                self.height=height
                self.side1=side1
                self.side2=side2

            def Trapezium_Area(self):
                return (0.5*(self.side1+self.side2)*self.height)

        x=float(input("Give length of first parallel side:"))
        y=float(input("Give length of second parallel side:"))
        z=float(input("Give length of height:"))

        obj=Trapezium(x,y,z)
        print("Area of Trapezium is:",obj.Trapezium_Area())

    elif name=="rectangle":
        class Rectangle():
            def __init__(self,length ,breadth):
                self.length=length
                self.breadth=breadth

            def Rectangle_Area(self):
                return self.length*self.breadth

        m=float(input("Give length of length:"))
        n=float(input("Give length of breadth:"))

        obj=Rectangle(m,n)
        print("Area of rectangle is:",obj.Rectangle_Area())

    elif name=="square":
        class Square():
            def __init__(self,length):
                self.length=length

            def Square_Area(self):
                return self.length**2

        side=float(input("Give length of side:"))

        obj=Square(side)
        print("Area of square is:",obj.Square_Area())

    elif name=="rhombus":
        class Rhombus():
            def __init__(self,diagonal1,diagonal2):
                self.diagonal1=diagonal1
                self.diagonal2=diagonal2

            def Rhombus_Area(self):
               return (0.5*self.diagonal1*self.diagonal2)

        x=float(input("Give length of first diagonal:"))
        y=float(input("Give length of second diagonal:"))

        obj=Rhombus(x,y)
        print("Area of rhumbus is:",obj.Rhombus_Area())

    elif name=="circle":
        class Circle():
            def __init__(self,radius):
                self.radius=radius

            def Circle_Area(self):
                return math.pi*self.radius**2
        r=float(input("Give radius of circle:"))

        obj=Circle(r)
        print("Area of circle is:",obj.Circle_Area())

    elif name=="semicircle":
        class Semicircle():
            def __init__(self,radius):
                self.radius=radius

            def Semicircle_Area(self):
                return (math.pi*self.radius**2)/2

        r=float(input("Give radius of semicircle:"))

        obj=Semicircle(r)
        print("Area of semicircle is:",obj.Semicircle_Area())

    elif name=="ellipse":
        class Ellipse():
            def __init__(self,major_axis,minor_axis):
                self.major_axis=major_axis
                self.minor_axis=minor_axis

            def Ellipse_Area(self):
                return math.pi*self.major_axis*self.minor_axis

        a=float(input("Give length of major axis:"))
        b=float(input("Give length of minor axis:"))

        obj=Ellipse(a,b)
        print("Area of ellipse is:",obj.Ellipse_Area())

    elif name=="sphere":
        class Sphere():
            def __init__(self,radius):
                self.radius=radius

            def Sphere_Area(self):
                return 4*math.pi*self.radius**2

        r=float(input("Give radius of sphere:"))

        obj=Sphere(r)
        print("Total surface area of sphere is:",obj.Sphere_Area())

    elif name=="hemisphere":
        class Hemisphere():
            def __init__(self,radius):
                self.radius=radius

            def Hemisphere_Area(self):
                return 3*math.pi*self.radius**2

        r=float(input("Give radius of hemisphere:"))

        obj=Hemisphere(r)
        print("Total surface area of hemisphere is:",obj.Hemisphere_Area())

    elif name=="cone":
        class Cone():
            def __init__(self,radius,slant_height):
                self.radius=radius
                self.slant_height=slant_height

            def Curve_Area(self):
                return 2*math.pi*self.radius*self.slant_height

            def Base_Area(self):
                return math.pi*self.radius**2

            def Total_Area(self):
                return (2*math.pi*self.radius*self.slant_height+math.pi*self.radius**2)

        r=float(input("Give length of radius:"))
        l=float(input("Give length of slant height:"))

        obj=Cone(r,l)
        print("Area of curve surface of cone is:",obj.Curve_Area())
        print("Area of base of cone is:",obj.Base_Area())
        print("Total surface area of cone is:",obj.Total_Area())

    elif name=="cylinder":
        class Cylinder():
            def __init__(self,radius,height):
                self.radius=radius
                self.height=height

            def Curve_Area(self):
                return 2*math.pi*self.radius*self.height

            def Base_Area(self):
                return 2*math.pi*self.radius**2

            def Total_Area(self):
                return 2*math.pi*self.radius*(self.radius+self.height)

        r=float(input("Give radius of cylinder:"))
        h=float(input("Give height of cylinder:"))

        obj=Cylinder(r,h)
        print("Area of curve surface of cylinder is:",obj.Curve_Area())
        print("Area of base of cylinder is:",obj.Base_Area())
        print("Total surface area of cylinder is:",obj.Total_Area())

    elif name=="rectangularprism":
        class RectangularPrism():
            def __init__(self,length,breadth,height):
                self.length=length
                self.breadth=breadth
                self.height=height

            def Total_Area(self):
                return 2*(self.length*self.breadth+self.breadth*self.height+self.height*self.length)

        l=float(input("Enter length of rectangular prism:"))
        b=float(input("Enter breadth of reactangular prism:"))
        h=float(input("Enter height of rectangular prism:"))

        obj=RectangularPrism(l,b,h)
        print("Total surface area of rectangular prism is:",obj.Total_Area())

    elif name=="cube":
        class Cube():
            def __init__(self,side):
                self.side=side

            def Cube_Area(self):
                return 6*self.side**2

        s=float(input("Give side of cube:"))

        obj=Cube(s)
        print("Total surface area of cube is:",obj.Cube_Area())
        
    else:
        print("Cant find the area of this shape!!")

if __name__ == "__main__":

    print("Calculate Shape Area")
    Shape_name=input("Give the shape:")
    calculate_area(Shape_name)
