a=int(input("Enter the first digit: "))
b=int(input("Enter the second digit: "))
c=int(input("Enter the third digit: "))
print("The all combination of numbers are:")
num1=a*100+b*10+c
print(num1)
num2=a*100+c*10+b
print(num2)
num3=b*100+c*10+a
print(num3)
num4=b*100+a*10+c
print(num4)
num5=c*100+a*10+b
print(num5)
num6=c*100+b*10+a
print(num6)
