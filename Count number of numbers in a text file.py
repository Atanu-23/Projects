fp=open("Textfile.txt","w+")
n=int(input("Enter number of characters:"))
m=int(input("Enter number of numbers:"))
l1=[]
l2=[]
for i in range(n):
    character=input("Enter word"+str(i+1)+":")
    l1.append(character)
fp.write("Contents of file is:\n")
fp.writelines(l1)
for i in range(m):
    number=input("Enter number"+str(i+1)+":")
    l2.append(number)
fp.writelines(l2)
fp.close()

with open("Textfile.txt","r+")as fp:
    print("The output of file is:",fp.read())
print()

count=0
with open("Textfile.txt","r+")as fp:
    lines=fp.read()
    numbers=lines.split(",")
    for number in numbers:
        if number.isnumeric()==True:
            count+=1
print("Number of numbers in textfile is:",count)            
            
