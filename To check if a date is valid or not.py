dd=0
mm=0
yy=0
date=input("Enter a date: ")
dd,mm,yy=date.split('-')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    if dd<=31:
        print("The date is valid")
    else:
        print("The date is invalid")
elif(mm==4 or mm==6 or mm==9 or mm==11):
    if dd<=30:
        print("The date is valid")
    else:
        print("The date is invalid")
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    if mm==2:
        if dd<=29:
            print("The date is valid")
        else:
            print("The date is invalid")
elif(mm==2):
    if dd<=28:
        print("The date is valid")
    else:
        print("The date is invalid")    

else:
    print("Date is invalid")
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or (mm==12 and dd!=31)):
    if dd<31:
        dd=dd+1
        mm=mm
        yy=yy
    else:
        dd=dd
        mm=mm+1
        yy=yy
    u=str(dd)
    v=str(mm)
    w=str(yy)
    strl=(u,v,w)
    date='-'.join(strl)    
    print("The increament of date is: ",date)
    
elif(mm==4 or mm==6 or mm==9 or mm==11):
    if dd<30:
        dd=dd+1
        mm=mm
        yy=yy
    else:
        dd=dd
        mm=mm+1
        yy=yy
    u=str(dd)
    v=str(mm)
    w=str(yy)
    strl=(u,v,w)
    date='-'.join(strl)    
    print("The increament of date is: ",date)
    
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    if(mm==2 and dd<=29):
        if dd<29:
            dd=dd+1
            mm=mm
            yy=yy  
        else:
            dd=dd
            mm=mm+1
            yy=yy
    elif(dd==31 and mm==12):
        dd=1
        mm=1
        yy=yy+1
    else:
        print('\n')
    u=str(dd)
    v=str(mm)
    w=str(yy)
    strl=(u,v,w)
    date='-'.join(strl)    
    print("The increament of date is: ",date)
    
elif (mm==2):
    if dd<28:
        dd=dd+1
        mm=mm
        yy=yy
    u=str(dd)
    v=str(mm)
    w=str(yy)
    strl=(u,v,w)
    date='-'.join(strl)    
    print("The increament of date is: ",date)
    
elif (dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    u=str(dd)
    v=str(mm)
    w=str(yy)
    strl=(u,v,w)
    date='-'.join(strl)
    print("The increament of date is: ",date)
    
else:
    print("The date is invalid")
        
