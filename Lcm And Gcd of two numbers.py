a=float(input("ENTER THE NUMBER: "))
b=float(input("ENTER THE NUMBER: "))
M=0
p=a
q=b
if a>b:
    max=a
else:
    max=b

while(True):
    if(max%a==0 and max%b==0):
        print("THE LCM OF TWO NUMBERS %f"%a,"AND %f"%b,"IS: ",max)
        break
    max=max+1
M=(p*q)/max
print("THE HCF OF TWO NUMBERS %f"%p,"AND %f"%q,"IS: ",M)
