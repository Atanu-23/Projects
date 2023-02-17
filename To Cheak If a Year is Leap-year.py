Y=int(input("Enter the year: "))
if(Y%4==0 and Y%100!=0 or Y%400==0):
    print("The year is leap-year")
else:
    print("The year is not leap-year")
