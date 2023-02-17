def Product(a,b):

    if a==0 or b==0:
        return 0
    else:
        return a*b

def Power(a,b):

    if a==0:
        return 0
    elif b==0:
        return 1
    else:
        return a**b
  
first_number=int(input("Give first number:"))
print()
second_number=int(input("Give second number:"))
print()
print("Product of "+str(first_number)+" and "+str(second_number)+" is:",Product(first_number,second_number))
print()
print("Power of "+str(first_number)+" and "+str(second_number)+" is:",Power(first_number,second_number))


