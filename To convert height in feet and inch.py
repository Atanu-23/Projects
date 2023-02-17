H=int(input("Enter the height in centimeter: "))
T=H*0.3937
Ft=T//12
Inch=T%12
a=str("%f feet"%Ft)
b=str("%f inch"%Inch)
c=a+' '+b
print("The height in feet and inch is: %s"%c)
