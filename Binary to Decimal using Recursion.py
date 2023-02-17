def ConvertBinary(decimal):

    if decimal==0:
        return 0
    else:
        return decimal%2+10*(ConvertBinary(int(decimal//2)))

decimal_number=int(input("Give the decimal number:"))
print()
print("Binary number of "+str(decimal_number)+" is:",ConvertBinary(decimal_number))
print()

def ConvertDecimaltoBinary(decimal):

    if decimal==0:
        return 0

    smallanswer=ConvertDecimaltoBinary(decimal//2)

    return decimal%2+10*smallanswer

decimal_number=int(input("Give the decimal number:"))
print()
print("Binary number of "+str(decimal_number)+" is:",ConvertDecimaltoBinary(decimal_number)) 
